# -*- coding: utf-8 -*-
# Module: widevine_keys
# Created on: 10.12.2021
# Authors: medvm
# Version: 2.1.0

import base64, requests, sys, xmltodict
import headers
import json
from cdm import cdm, deviceconfig
from base64 import b64encode
from getPSSH import get_pssh
from wvdecryptcustom import WvDecrypt
from cdm.formats import wv_proto2_pb2 as wv_proto2
from urllib.parse import urlparse
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, Application,CallbackContext
import logging
# logging.basicConfig(level=logging.DEBUG)
# pssh = input('\nPSSH: ')
lic_url = 'https://sdrm.tv360.vn/license/verify/widevine'
responses = []
license_b64 = ''

# print(f'{chr(10)}PSSH obtained.\n{pssh}')

def WV_Function(pssh, lic_url, cert_b64=None):
	wvdecrypt = WvDecrypt(init_data_b64=pssh, cert_data_b64=cert_b64, device=deviceconfig.device_android_generic)                   
	raw_request = wvdecrypt.get_challenge()
	request = b64encode(raw_request)
	signature = cdm.hash_object
# basic, mostly sites works
	responses.append(requests.post(url=lic_url, headers=headers.headers, data=raw_request))
	for idx, response in enumerate(responses):
		try:
			str(response.content, "utf-8")
		except UnicodeDecodeError:
			widevine_license = response
			print(f'{chr(10)}license response status: {widevine_license}{chr(10)}')
			break	
		else:
			if len(str(response.content, "utf-8")) > 500:
				widevine_license = response
				print(f'{chr(10)}license response status: {widevine_license}{chr(10)}')
				break
		if idx == len(responses) - 1:
			print(f'{chr(10)}license response status: {response}')
			print(f'server reports: {str(response.content, "utf-8")}')
			print(f'server did not issue license, make sure you have correctly pasted all the required headers in the headers.py. Also check json/raw params of POST request.{chr(10)}')
			exit() 	
		
	lic_field_names = ['license', 'payload', 'getWidevineLicenseResponse']
	lic_field_names2 = ['license']
	
	open('license_content.bin', 'wb').write(widevine_license.content)

	try:
		if str(widevine_license.content, 'utf-8').find(':'):
			for key in lic_field_names:
				try: 
					license_b64 = json.loads(widevine_license.content.decode())[key]
				except:
					pass			
				else:
					for key2 in lic_field_names2:
						try: 
							license_b64 = json.loads(widevine_license.content.decode())[key][key2]
						except:
							pass
		else:
			license_b64 = widevine_license.content								
	except:
		license_b64 = b64encode(widevine_license.content)

	wvdecrypt.update_license(license_b64)
	Correct, keyswvdecrypt = wvdecrypt.start_process()
	if Correct:
		return Correct, keyswvdecrypt

# correct, keys = WV_Function(pssh, lic_url)
#
# for key in keys:
# 	print('KID:KEY -> ' + key)


async def hello(update: Update, context:ContextTypes.DEFAULT_TYPE) -> None:
	pssh = str({update.effective_message.text.replace("/getkey","")})
	pssh = pssh.replace(' ','')
	lic_url = 'https://sdrm.tv360.vn/license/verify/widevine'
	responses = []
	license_b64 = ''
	correct, keys = WV_Function(pssh, lic_url)
	for key in keys:
		await update.message.reply_text(f'{key} ')

async def error(update: Update, context: CallbackContext):
    await update.message.reply_text(f'{context.error}')

app = Application.builder().token('6817570334:AAGNhnC3AD2VRW-eWjX5BawBiPap9sb5tlw').build()

app.add_handler(CommandHandler("getkey", hello))

app.add_error_handler(error)

app.run_polling()



