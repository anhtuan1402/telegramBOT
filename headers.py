import requests

headers = {
    'Accept': '*/*',
    'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7,fr-FR;q=0.6,fr;q=0.5',
    'Connection': 'keep-alive',
    'Origin': 'https://tv360.vn',
    'Referer': 'https://tv360.vn/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'content-type': 'application/octet-stream',
    'custom-data': 'eyJ1c2VySWQiOiIxNTUwMjIxMyIsInNlc3Npb25JZCI6ImV5SmhiR2NpT2lKSVV6STFOaUo5LmV5SnFkR2tpT2lJeE5UVXdNakl4TXlJc0luTmthU0k2SW50Y0luVnpaWEpjSWpwY0lqRTFOVEF5TWpFelhDSXNYQ0p0WlhKamFHRnVkRndpT2x3aWRtbGxkSFJsYkhaaGMxd2lMRndpWVhOelpYUmNJanBjSW5aMGRtTmhZakUyWDJoa1h6VXdabkJ6WENKOUlpd2lhV0YwSWpveE5qazROVGsxTVRrekxDSmxlSEFpT2pFMk9Ua3hPVFV4T1ROOS43QUExSXcyeXNwb0FVRnU0UlBHci1hNlI3RWVzT2tfZXA4RGNNX20zUXdFIiwibWVyY2hhbnRJZCI6InZpZXR0ZWx2YXMiLCJhcHBJZCI6IlRWMzYwIiwicmVxSWQiOiI1Y2FhNjQ1MC0yNzBmLTMyZTAtNGRiYy04NTFlMDgxMjdlYWMiLCJkZXZpY2VJbmZvIjoie1wic2lnbmF0dXJlXCI6XCJBRjQ0MjhCODMyNzdEQTU1QTUxODM1NDFDRUE2NDAyOUYzRDcwNEZGXCIsXCJhcHBWZXJzaW9uQ29kZVwiOjM0MCxcImFwcFZlcnNpb25cIjpcIjMuNFwiLFwicGFja2FnZUlkXCI6XCJjb20udmlldHRlbC50djM2MC50dlwiLFwiYnVpbGRCb2FyZFwiOlwicGljYXNzb1wiLFwiYnVpbGRIb3N0XCI6XCJ4aWFvbWkuZXVcIixcInBhY2thZ2VOYW1lXCI6XCJUVjM2MFwiLFwic2RrVmVyc2lvblwiOlwiMzBcIixcImRldmljZUlkXCI6XCI0YmNkZmM3N2U4ZGNkYzQwXCIsXCJkZXZpY2VNb2RlbFwiOlwiUmVkbWkgSzMwIDVHIFNwZWVkXCIsXCJwYWNrZXJWZXJzaW9uXCI6XCIxLjAuM1wiLFwiYnJhbmRcIjpcIlJlZG1pXCIsXCJvc1ZlcnNpb25cIjpcIjExXCIsXCJidWlsZFByb2R1Y3RcIjpcInBpY2Fzc29cIixcIm1hbnVmYWN0dXJlXCI6XCJYaWFvbWlcIixcImNwdUluZm9cIjpcInFjb21cIixcIm9zQnVpbGRcIjpcIlJLUTEuMjAwODI2LjAwMiByZWxlYXNlLWtleXNcIixcInBsYXRmb3JtXCI6XCJhbmRyb2lkXCIsXCJkZXZpY2VOYW1lXCI6XCJwaWNhc3NvXCIsXCJmaW5nZXJwcmludFwiOlwiUmVkbWlcL3BpY2Fzc29cL3BpY2Fzc286MTFcL1JLUTEuMjAwODI2LjAwMlwvVjEyLjUuNS4wLlJHSUNOWE06dXNlclwvcmVsZWFzZS1rZXlzXCJ9In0='
}
