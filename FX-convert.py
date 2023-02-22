from flask import Flask, request

app = Flask(__name__)

@app.route("/result", methods=["POST", "GET"])
def result():
    output = request.get_json()
    bank = output["BAN"][0:3]
    info = {'003': ' Standard Chartered Bank (Hong Kong) Limited', '004': ' The Hongkong and Shanghai Banking Corporation Limited', '005': ' Credit Agricole Corporate and Investment Bank', '006': ' Citibank, N.A.', '007': ' JPMorgan Chase Bank, N.A.', '008': ' NatWest Markets Plc', '009': ' China Construction Bank (Asia) Corporation Limited', '012': ' Bank of China (Hong Kong) Limited', '015': ' The Bank of East Asia, Ltd.', '016': ' DBS Bank (Hong Kong) Limited', '018': ' China CITIC Bank International Limited', '020': ' CMB Wing Lung Bank Limited', '022': ' Oversea-Chinese Banking Corporation Ltd.', '024': ' Hang Seng Bank Ltd.', '025': ' Shanghai Commercial Bank Limited', '027': ' Bank of Communications Co., Ltd.', '028': ' Public Bank (Hong Kong) Limited', '035': ' OCBC Wing Hang Bank Limited', '038': ' Tai Yau Bank Limited', '039': ' Chiyu Banking Corporation Ltd.', '040': ' Dah Sing Bank, Ltd.', '041': ' Chong Hing Bank Limited', '043': ' Nanyang Commercial Bank Limited', '045': ' UCO Bank', '046': ' KEB Hana Bank', '047': ' MUFG Bank, Ltd.', '049': ' Bangkok Bank Public Company Limited', '050': ' Indian Overseas Bank', '054': ' Deutsche Bank AG', '055': ' Bank of America, N.A.', '056': ' BNP Paribas', '058': ' Bank of India', '060': ' National Bank of Pakistan', '061': ' Tai Sang Bank Limited', '063': ' Malayan Banking Berhad (Maybank)', '065': ' Sumitomo Mitsui Banking Corporation', '066': ' PT. Bank Negara Indonesia (Persero) Tbk.', '067': ' BDO Unibank, Inc.', '071': ' United Overseas Bank Limited', '072': ' Industrial and Commercial Bank of China (Asia) Limited', '074': ' Barclays Bank Plc.', '076': ' The Bank of Nova Scotia', '080': ' Royal Bank of Canada', '081': ' Societe Generale', '082': ' State Bank of India', '085': ' The Toronto-Dominion Bank', '086': ' Bank of Montreal', '092': ' Canadian Imperial Bank of Commerce', '097': ' Commerzbank AG', '103': ' UBS AG, Hong Kong', '106': ' HSBC Bank', '109': ' Mizuho Bank, Ltd., Hong Kong Branch', '113': ' DZ BANK AG Deutsche Zentral-Genossenschaftsbank', '118': ' Woori Bank', '119': ' Philippine National Bank', '128': ' Fubon Bank (Hong Kong) Limited', '138': ' Mitsubishi UFJ Trust and Banking Corporation', '139': ' The Bank of New York Mellon', '145': ' ING Bank N.V.', '147': ' Banco Bilbao Vizcaya Argentaria, S.A.', '150': ' National Australia Bank Limited', '151': ' Westpac Banking Corporation', '152': ' Australia and New Zealand Banking Group Ltd', '153': ' Commonwealth Bank of Australia', '161': ' Intesa Sanpaolo S.p.A.', '164': ' UniCredit Bank AG', '170': ' The Chiba Bank Limited', '178': ' KBC Bank N.V.', '180': ' Wells Fargo Bank, N.A.', '183': ' Coöperatieve Rabobank U.A.', '185': ' DBS Bank Ltd, Hong Kong Branch', '186': ' The Shizuoka Bank Ltd.', '188': ' The Hachijuni Bank, Ltd.', '198': ' Hua Nan Commercial Bank, Ltd.', '199': ' The Shiga Bank, Ltd.', '201': ' Bank of Taiwan', '202': ' The Chugoku Bank Limited', '203': ' First Commercial Bank', '206': ' Chang Hwa Commercial Bank, Ltd.', '210': ' Natixis', '214': ' Industrial and Commercial Bank of China Limited', '220': ' State Street Bank and Trust Company', '221': ' China Construction Bank Corporation', '222': ' Agricultural Bank of China Limited', '227': ' Erste Group Bank AG', '229': ' CTBC Bank Co., Ltd.', '230': ' Taiwan Business Bank, Ltd.', '233': ' Credit Suisse AG', '236': ' Cathay United Bank Company, Limited', '237': ' EFG Bank AG', '238': ' China Merchants Bank Co., Ltd.', '239': ' Taipei Fubon Commercial Bank Co., Ltd.', '241': ' Bank SinoPac', '242': ' Mega International Commercial Bank Co., Ltd.', '243': ' E.Sun Commercial Bank, Ltd.', '245': ' Taishin International Bank Co., Ltd.', '248': ' Hong Leong Bank Berhad', '249': ' Standard Chartered Bank Hong Kong Branch', '250': ' Citibank (Hong Kong) Limited', '251': ' ICICI Bank Limited', '254': ' Melli Bank plc', '258': ' East West Bank', '260': ' Far Eastern International Bank', '263': ' Cathay Bank', '264': ' Land Bank of Taiwan Co., Ltd.', '265': ' Taiwan Cooperative Bank, Ltd.', '266': ' Punjab National Bank', '267': ' Banco Santander S.A.', '268': ' Union Bank of India', '269': ' The Shanghai Commercial & Savings Bank, Ltd.', '271': ' Industrial Bank of Korea', '272': ' Bank of Singapore Limited', '273': ' Shinhan Bank', '274': ' O-Bank Co., Ltd.', '275': ' BNP Paribas Securities Services', '276': ' China Development Bank', '277': ' First Abu Dhabi Bank PJSC', '278': ' Bank J. Safra Sarasin Ltd.', '307': ' ABN AMRO Bank N.V.', '308': ' HDFC Bank Limited', '309': ' Union Bancaire Privée, UBP SA', '316': ' Skandinaviska Enskilda Banken AB', '320': ' Bank Julius Baer & Co. Ltd.', '324': ' Credit Industriel et Commercial', '337': ' Taiwan Shin Kong Commercial Bank Co., Ltd.', '338': ' Bank of China Limited, Hong Kong Branch', '339': ' CA Indosuez (Switzerland) SA', '342': ' LGT Bank AG', '345': ' Shanghai Pudong Development Bank Co., Ltd.', '353': ' China Minsheng Banking Corp., Ltd.', '359': ' China Guangfa Bank Co., Ltd.', '361': ' China Bohai Bank Co., Ltd.', '364': ' Banque Pictet & Cie SA', '365': ' Bank of Dongguan Co., Ltd.', '368': ' China Everbright Bank Co., Ltd.', '371': ' Sumitomo Mitsui Trust Bank, Limited', '372': ' Bank of Shanghai (Hong Kong) Limited', '374': ' CIMB Bank Berhad', '376': ' NongHyup Bank', '377': ' Industrial Bank Co., Ltd.', '378': ' Yuanta Commercial Bank Co., Ltd.', '379': ' Mashreq Bank - Public Shareholding Company', '381': ' Kookmin Bank', '382': ' Bank of Communications (Hong Kong) Limited', '383': ' China Zheshang Bank Co., Ltd.', '384': ' Morgan Stanley Bank Asia Limited', '385': ' Ping An Bank Co., Ltd.', '386': ' Hua Xia Bank Co., Limited', '387': ' ZA Bank Limited', '388': ' Livi Bank Limited', '389': ' Mox Bank Limited', '390': ' Welab Bank Limited', '391': ' Fusion Bank Limited', '392': ' Ping An OneConnect Bank (Hong Kong) Limited', '393': ' Ant Bank (Hong Kong) Limited', '394': ' Qatar National Bank (Q.P.S.C.)', '395': ' Airstar Bank Limited', '802': ' Hong Kong Securities Clearing Company Limited', '868': ' CLS Bank International'}
    #cc = {'UK': 'GBP', 'AF': 'AFN', 'AX': 'EUR', 'AL': 'ALL', 'DZ': 'DZD', 'AS': 'USD', 'AD': 'EUR', 'AO': 'AOA', 'AI': 'XCD', 'AG': 'XCD', 'AR': 'ARS', 'AM': 'AMD', 'AW': 'AWG', 'AU': 'AUD', 'AT': 'EUR', 'AZ': 'AZN', 'BS': 'BSD', 'BH': 'BHD', 'BD': 'BDT', 'BB': 'BBD', 'BY': 'BYN', 'BE': 'EUR', 'BZ': 'BZD', 'BJ': 'XOF', 'BM': 'BMD', 'BT': 'BTN', 'BO': 'BOB', 'BQ': 'USD', 'BA': 'BAM', 'BW': 'BWP', 'BV': 'NOK', 'BR': 'BRL', 'IO': 'USD', 'BN': 'BND', 'BG': 'BGN', 'BF': 'XOF', 'BI': 'BIF', 'KH': 'CVE', 'CM': 'KHR', 'CA': 'XAF', 'CV': 'CAD', 'KY': 'KYD', 'CF': 'XAF', 'TD': 'XAF', 'CL': 'CLF', 'CN': 'CNY', 'CX': 'AUD', 'CC': 'AUD', 'CO': 'COP', 'KM': 'KMF', 'CG': 'CDF', 'CD': 'XAF', 'CK': 'NZD', 'CR': 'CRC', 'CI': 'XOF', 'HR': 'HRK', 'CU': 'CUC', 'CW': 'ANG', 'CY': 'EUR', 'CZ': 'CZK', 'DK': 'DKK', 'DJ': 'DJF', 'DM': 'XCD', 'DO': 'DOP', 'EC': 'USD', 'EG': 'EGP', 'SV': 'USD', 'GQ': 'XAF', 'ER': 'ERN', 'EE': 'EUR', 'ET': 'ETB', 'FK': 'FKP', 'FO': 'DKK', 'FJ': 'FJD', 'FI': 'EUR', 'FR': 'EUR', 'GF': 'EUR', 'PF': 'XPF', 'TF': 'EUR', 'GA': 'XAF', 'GM': 'GMD', 'GE': 'GEL', 'DE': 'EUR', 'GH': 'GHS', 'GI': 'GIP', 'GR': 'EUR', 'GL': 'DKK', 'GD': 'XCD', 'GP': 'EUR', 'GU': 'USD', 'GT': 'GTQ', 'GG': 'GBP', 'GN': 'GNF', 'GW': 'XOF', 'GY': 'GYD', 'HT': 'USD', 'HM': 'AUD', 'VA': 'EUR', 'HN': 'HNL', 'HK': 'HKD', 'HU': 'HUF', 'IS': 'ISK', 'IN': 'INR', 'ID': 'IDR', 'IR': 'IRR', 'IQ': 'IQD', 'IE': 'EUR', 'IM': 'GBP', 'IL': 'ILS', 'IT': 'EUR', 'JM': 'JMD', 'JP': 'JPY', 'JE': 'GBP', 'JO': 'JOD', 'KZ': 'KZT', 'KE': 'KES', 'KI': 'AUD', 'KP': 'KPW', 'KR': 'KRW', 'KW': 'KWD', 'KG': 'KGS', 'LA': 'LAK', 'LV': 'EUR', 'LB': 'LBP', 'LS': 'ZAR', 'LR': 'LRD', 'LY': 'LYD', 'LI': 'CHF', 'LT': 'EUR', 'LU': 'EUR', 'MO': 'MOP', 'MK': 'MKD', 'MG': 'MGA', 'MW': 'MWK', 'MY': 'MYR', 'MV': 'MVR', 'ML': 'XOF', 'MT': 'EUR', 'MH': 'USD', 'MQ': 'EUR', 'MR': 'MRU', 'MU': 'MUR', 'YT': 'EUR', 'MX': 'MXN', 'FM': 'USD', 'MD': 'MDL', 'MC': 'EUR', 'MN': 'MNT', 'ME': 'EUR', 'MS': 'XCD', 'MA': 'MAD', 'MZ': 'MZN', 'MM': 'MMK', 'ZA': 'SBD', 'NR': 'AUD', 'NP': 'NPR', 'NL': 'EUR', 'NC': 'XPF', 'NZ': 'NZD', 'NI': 'NIO', 'NE': 'XOF', 'NG': 'NGN', 'NU': 'NZD', 'NF': 'AUD', 'MP': 'USD', 'NO': 'NOK', 'OM': 'OMR', 'PK': 'PKR', 'PW': 'USD', 'PA': 'PAB', 'PG': 'USD', 'PY': 'PGK', 'PE': 'PYG', 'PH': 'PEN', 'PN': 'PHP', 'PL': 'NZD', 'PT': 'PLN', 'PR': 'EUR', 'QA': 'USD', 'RE': 'QAR', 'RO': 'EUR', 'RU': 'RON', 'RW': 'RUB', 'BL': 'RWF', 'SH': 'EUR', 'KN': 'SHP', 'LC': 'XCD', 'MF': 'XCD', 'PM': 'EUR', 'VC': 'EUR', 'WS': 'XCD', 'SM': 'WST', 'ST': 'EUR', 'SA': 'STN', 'SN': 'SAR', 'RS': 'XOF', 'SC': 'RSD', 'SL': 'SCR', 'SG': 'SLL', 'SX': 'SGD', 'SK': 'ANG', 'SI': 'XSU', 'SB': 'EUR', 'SO': 'EUR', 'GS': 'SOS', 'SS': 'ZAR', 'LK': 'SSP', 'ES': 'EUR', 'SR': 'LKR', 'SJ': 'SDG', 'SZ': 'SRD', 'SE': 'SEK', 'CH': 'CHF', 'SY': 'SYP', 'TW': 'TWD', 'TJ': 'TJS', 'TZ': 'TZS', 'TH': 'THB', 'TL': 'USD', 'TG': 'XOF', 'TK': 'NZD', 'TO': 'TOP', 'TT': 'TTD', 'TN': 'TND', 'TR': 'TRY', 'TM': 'TMT', 'TC': 'USD', 'TV': 'AUD', 'UG': 'UGX', 'UA': 'UAH', 'AE': 'AED', 'GB': 'GBP', 'UM': 'USD', 'US': 'USD', 'UY': 'UYW', 'UZ': 'UZS', 'VU': 'VUV', 'VE': 'VES', 'VN': 'VND', 'VG': 'USD', 'VI': 'USD', 'WF': 'XPF', 'EH': 'MAD', 'YE': 'YER', 'ZM': 'ZMW', 'ZW': 'ZWL'}
    banks = {
    "106": {'bank_name': 'HSBC', 'FX': {
        'EUR': 1.07,
        'USD': 1.14,
        'TRY': 21.24,
        'AUD': 1.62,
        'BD': 0.42,
        'BBD': 2.23,
        'AED': 4.11,
        'CHF': 1.01,
        'SEK': 11.43,
        'SGD': 1.47,
        'SAU': 4.12,
        'JPY': 152.80,
        'HKD': 8.78,
        'CNY': 7.62,
        'CAD': 1.54
    }},
    "074": {'bank_name': 'BARCLAYS', 'FX': {
        'EUR': 1.07,
        'USD': 1.14,
        'TRY': 20.63,
        'AUD': 1.64,
        'BD': 0.42,
        'BBD': 2.19,
        'AED': 4.14,
        'CHF': 1.05,
        'SEK': 11.88,
        'SGD': 1.51,
        'SAU': 4.24,
        'JPY': 153.81,
        'HKD': 8.93,
        'CNY': 7.47,
        'CAD': 1.52
    }}
    }
    amount = float(output["amount"])
    currency = output["C"]
    value = str(round(banks[bank]['FX'][currency]*amount, 2))

    if bank in info and len(output["BAN"]) == 10:
        return 'Your bank is, ' + info[bank] + '. The current exchange rate for ' + currency + ' is  ' + str(banks[bank]['FX'][currency]) + '. So, for ' + str(amount) + ' GBP you will get ' + value + ' '+ currency

    else:
        return "Invalid Bank Account Number. Please try again."
  
@app.route("/fx-rates", methods=["GET"])
def fx_rates():
    output = request.get_json()
    bank = output["BAN"][0:3]
    info = {'003': ' Standard Chartered Bank (Hong Kong) Limited', '004': ' The Hongkong and Shanghai Banking Corporation Limited', '005': ' Credit Agricole Corporate and Investment Bank', '006': ' Citibank, N.A.', '007': ' JPMorgan Chase Bank, N.A.', '008': ' NatWest Markets Plc', '009': ' China Construction Bank (Asia) Corporation Limited', '012': ' Bank of China (Hong Kong) Limited', '015': ' The Bank of East Asia, Ltd.', '016': ' DBS Bank (Hong Kong) Limited', '018': ' China CITIC Bank International Limited', '020': ' CMB Wing Lung Bank Limited', '022': ' Oversea-Chinese Banking Corporation Ltd.', '024': ' Hang Seng Bank Ltd.', '025': ' Shanghai Commercial Bank Limited', '027': ' Bank of Communications Co., Ltd.', '028': ' Public Bank (Hong Kong) Limited', '035': ' OCBC Wing Hang Bank Limited', '038': ' Tai Yau Bank Limited', '039': ' Chiyu Banking Corporation Ltd.', '040': ' Dah Sing Bank, Ltd.', '041': ' Chong Hing Bank Limited', '043': ' Nanyang Commercial Bank Limited', '045': ' UCO Bank', '046': ' KEB Hana Bank', '047': ' MUFG Bank, Ltd.', '049': ' Bangkok Bank Public Company Limited', '050': ' Indian Overseas Bank', '054': ' Deutsche Bank AG', '055': ' Bank of America, N.A.', '056': ' BNP Paribas', '058': ' Bank of India', '060': ' National Bank of Pakistan', '061': ' Tai Sang Bank Limited', '063': ' Malayan Banking Berhad (Maybank)', '065': ' Sumitomo Mitsui Banking Corporation', '066': ' PT. Bank Negara Indonesia (Persero) Tbk.', '067': ' BDO Unibank, Inc.', '071': ' United Overseas Bank Limited', '072': ' Industrial and Commercial Bank of China (Asia) Limited', '074': ' Barclays Bank Plc.', '076': ' The Bank of Nova Scotia', '080': ' Royal Bank of Canada', '081': ' Societe Generale', '082': ' State Bank of India', '085': ' The Toronto-Dominion Bank', '086': ' Bank of Montreal', '092': ' Canadian Imperial Bank of Commerce', '097': ' Commerzbank AG', '103': ' UBS AG, Hong Kong', '106': ' HSBC Bank', '109': ' Mizuho Bank, Ltd., Hong Kong Branch', '113': ' DZ BANK AG Deutsche Zentral-Genossenschaftsbank', '118': ' Woori Bank', '119': ' Philippine National Bank', '128': ' Fubon Bank (Hong Kong) Limited', '138': ' Mitsubishi UFJ Trust and Banking Corporation', '139': ' The Bank of New York Mellon', '145': ' ING Bank N.V.', '147': ' Banco Bilbao Vizcaya Argentaria, S.A.', '150': ' National Australia Bank Limited', '151': ' Westpac Banking Corporation', '152': ' Australia and New Zealand Banking Group Ltd', '153': ' Commonwealth Bank of Australia', '161': ' Intesa Sanpaolo S.p.A.', '164': ' UniCredit Bank AG', '170': ' The Chiba Bank Limited', '178': ' KBC Bank N.V.', '180': ' Wells Fargo Bank, N.A.', '183': ' Coöperatieve Rabobank U.A.', '185': ' DBS Bank Ltd, Hong Kong Branch', '186': ' The Shizuoka Bank Ltd.', '188': ' The Hachijuni Bank, Ltd.', '198': ' Hua Nan Commercial Bank, Ltd.', '199': ' The Shiga Bank, Ltd.', '201': ' Bank of Taiwan', '202': ' The Chugoku Bank Limited', '203': ' First Commercial Bank', '206': ' Chang Hwa Commercial Bank, Ltd.', '210': ' Natixis', '214': ' Industrial and Commercial Bank of China Limited', '220': ' State Street Bank and Trust Company', '221': ' China Construction Bank Corporation', '222': ' Agricultural Bank of China Limited', '227': ' Erste Group Bank AG', '229': ' CTBC Bank Co., Ltd.', '230': ' Taiwan Business Bank, Ltd.', '233': ' Credit Suisse AG', '236': ' Cathay United Bank Company, Limited', '237': ' EFG Bank AG', '238': ' China Merchants Bank Co., Ltd.', '239': ' Taipei Fubon Commercial Bank Co., Ltd.', '241': ' Bank SinoPac', '242': ' Mega International Commercial Bank Co., Ltd.', '243': ' E.Sun Commercial Bank, Ltd.', '245': ' Taishin International Bank Co., Ltd.', '248': ' Hong Leong Bank Berhad', '249': ' Standard Chartered Bank Hong Kong Branch', '250': ' Citibank (Hong Kong) Limited', '251': ' ICICI Bank Limited', '254': ' Melli Bank plc', '258': ' East West Bank', '260': ' Far Eastern International Bank', '263': ' Cathay Bank', '264': ' Land Bank of Taiwan Co., Ltd.', '265': ' Taiwan Cooperative Bank, Ltd.', '266': ' Punjab National Bank', '267': ' Banco Santander S.A.', '268': ' Union Bank of India', '269': ' The Shanghai Commercial & Savings Bank, Ltd.', '271': ' Industrial Bank of Korea', '272': ' Bank of Singapore Limited', '273': ' Shinhan Bank', '274': ' O-Bank Co., Ltd.', '275': ' BNP Paribas Securities Services', '276': ' China Development Bank', '277': ' First Abu Dhabi Bank PJSC', '278': ' Bank J. Safra Sarasin Ltd.', '307': ' ABN AMRO Bank N.V.', '308': ' HDFC Bank Limited', '309': ' Union Bancaire Privée, UBP SA', '316': ' Skandinaviska Enskilda Banken AB', '320': ' Bank Julius Baer & Co. Ltd.', '324': ' Credit Industriel et Commercial', '337': ' Taiwan Shin Kong Commercial Bank Co., Ltd.', '338': ' Bank of China Limited, Hong Kong Branch', '339': ' CA Indosuez (Switzerland) SA', '342': ' LGT Bank AG', '345': ' Shanghai Pudong Development Bank Co., Ltd.', '353': ' China Minsheng Banking Corp., Ltd.', '359': ' China Guangfa Bank Co., Ltd.', '361': ' China Bohai Bank Co., Ltd.', '364': ' Banque Pictet & Cie SA', '365': ' Bank of Dongguan Co., Ltd.', '368': ' China Everbright Bank Co., Ltd.', '371': ' Sumitomo Mitsui Trust Bank, Limited', '372': ' Bank of Shanghai (Hong Kong) Limited', '374': ' CIMB Bank Berhad', '376': ' NongHyup Bank', '377': ' Industrial Bank Co., Ltd.', '378': ' Yuanta Commercial Bank Co., Ltd.', '379': ' Mashreq Bank - Public Shareholding Company', '381': ' Kookmin Bank', '382': ' Bank of Communications (Hong Kong) Limited', '383': ' China Zheshang Bank Co., Ltd.', '384': ' Morgan Stanley Bank Asia Limited', '385': ' Ping An Bank Co., Ltd.', '386': ' Hua Xia Bank Co., Limited', '387': ' ZA Bank Limited', '388': ' Livi Bank Limited', '389': ' Mox Bank Limited', '390': ' Welab Bank Limited', '391': ' Fusion Bank Limited', '392': ' Ping An OneConnect Bank (Hong Kong) Limited', '393': ' Ant Bank (Hong Kong) Limited', '394': ' Qatar National Bank (Q.P.S.C.)', '395': ' Airstar Bank Limited', '802': ' Hong Kong Securities Clearing Company Limited', '868': ' CLS Bank International'}
    #cc = {'UK': 'GBP', 'AF': 'AFN', 'AX': 'EUR', 'AL': 'ALL', 'DZ': 'DZD', 'AS': 'USD', 'AD': 'EUR', 'AO': 'AOA', 'AI': 'XCD', 'AG': 'XCD', 'AR': 'ARS', 'AM': 'AMD', 'AW': 'AWG', 'AU': 'AUD', 'AT': 'EUR', 'AZ': 'AZN', 'BS': 'BSD', 'BH': 'BHD', 'BD': 'BDT', 'BB': 'BBD', 'BY': 'BYN', 'BE': 'EUR', 'BZ': 'BZD', 'BJ': 'XOF', 'BM': 'BMD', 'BT': 'BTN', 'BO': 'BOB', 'BQ': 'USD', 'BA': 'BAM', 'BW': 'BWP', 'BV': 'NOK', 'BR': 'BRL', 'IO': 'USD', 'BN': 'BND', 'BG': 'BGN', 'BF': 'XOF', 'BI': 'BIF', 'KH': 'CVE', 'CM': 'KHR', 'CA': 'XAF', 'CV': 'CAD', 'KY': 'KYD', 'CF': 'XAF', 'TD': 'XAF', 'CL': 'CLF', 'CN': 'CNY', 'CX': 'AUD', 'CC': 'AUD', 'CO': 'COP', 'KM': 'KMF', 'CG': 'CDF', 'CD': 'XAF', 'CK': 'NZD', 'CR': 'CRC', 'CI': 'XOF', 'HR': 'HRK', 'CU': 'CUC', 'CW': 'ANG', 'CY': 'EUR', 'CZ': 'CZK', 'DK': 'DKK', 'DJ': 'DJF', 'DM': 'XCD', 'DO': 'DOP', 'EC': 'USD', 'EG': 'EGP', 'SV': 'USD', 'GQ': 'XAF', 'ER': 'ERN', 'EE': 'EUR', 'ET': 'ETB', 'FK': 'FKP', 'FO': 'DKK', 'FJ': 'FJD', 'FI': 'EUR', 'FR': 'EUR', 'GF': 'EUR', 'PF': 'XPF', 'TF': 'EUR', 'GA': 'XAF', 'GM': 'GMD', 'GE': 'GEL', 'DE': 'EUR', 'GH': 'GHS', 'GI': 'GIP', 'GR': 'EUR', 'GL': 'DKK', 'GD': 'XCD', 'GP': 'EUR', 'GU': 'USD', 'GT': 'GTQ', 'GG': 'GBP', 'GN': 'GNF', 'GW': 'XOF', 'GY': 'GYD', 'HT': 'USD', 'HM': 'AUD', 'VA': 'EUR', 'HN': 'HNL', 'HK': 'HKD', 'HU': 'HUF', 'IS': 'ISK', 'IN': 'INR', 'ID': 'IDR', 'IR': 'IRR', 'IQ': 'IQD', 'IE': 'EUR', 'IM': 'GBP', 'IL': 'ILS', 'IT': 'EUR', 'JM': 'JMD', 'JP': 'JPY', 'JE': 'GBP', 'JO': 'JOD', 'KZ': 'KZT', 'KE': 'KES', 'KI': 'AUD', 'KP': 'KPW', 'KR': 'KRW', 'KW': 'KWD', 'KG': 'KGS', 'LA': 'LAK', 'LV': 'EUR', 'LB': 'LBP', 'LS': 'ZAR', 'LR': 'LRD', 'LY': 'LYD', 'LI': 'CHF', 'LT': 'EUR', 'LU': 'EUR', 'MO': 'MOP', 'MK': 'MKD', 'MG': 'MGA', 'MW': 'MWK', 'MY': 'MYR', 'MV': 'MVR', 'ML': 'XOF', 'MT': 'EUR', 'MH': 'USD', 'MQ': 'EUR', 'MR': 'MRU', 'MU': 'MUR', 'YT': 'EUR', 'MX': 'MXN', 'FM': 'USD', 'MD': 'MDL', 'MC': 'EUR', 'MN': 'MNT', 'ME': 'EUR', 'MS': 'XCD', 'MA': 'MAD', 'MZ': 'MZN', 'MM': 'MMK', 'ZA': 'SBD', 'NR': 'AUD', 'NP': 'NPR', 'NL': 'EUR', 'NC': 'XPF', 'NZ': 'NZD', 'NI': 'NIO', 'NE': 'XOF', 'NG': 'NGN', 'NU': 'NZD', 'NF': 'AUD', 'MP': 'USD', 'NO': 'NOK', 'OM': 'OMR', 'PK': 'PKR', 'PW': 'USD', 'PA': 'PAB', 'PG': 'USD', 'PY': 'PGK', 'PE': 'PYG', 'PH': 'PEN', 'PN': 'PHP', 'PL': 'NZD', 'PT': 'PLN', 'PR': 'EUR', 'QA': 'USD', 'RE': 'QAR', 'RO': 'EUR', 'RU': 'RON', 'RW': 'RUB', 'BL': 'RWF', 'SH': 'EUR', 'KN': 'SHP', 'LC': 'XCD', 'MF': 'XCD', 'PM': 'EUR', 'VC': 'EUR', 'WS': 'XCD', 'SM': 'WST', 'ST': 'EUR', 'SA': 'STN', 'SN': 'SAR', 'RS': 'XOF', 'SC': 'RSD', 'SL': 'SCR', 'SG': 'SLL', 'SX': 'SGD', 'SK': 'ANG', 'SI': 'XSU', 'SB': 'EUR', 'SO': 'EUR', 'GS': 'SOS', 'SS': 'ZAR', 'LK': 'SSP', 'ES': 'EUR', 'SR': 'LKR', 'SJ': 'SDG', 'SZ': 'SRD', 'SE': 'SEK', 'CH': 'CHF', 'SY': 'SYP', 'TW': 'TWD', 'TJ': 'TJS', 'TZ': 'TZS', 'TH': 'THB', 'TL': 'USD', 'TG': 'XOF', 'TK': 'NZD', 'TO': 'TOP', 'TT': 'TTD', 'TN': 'TND', 'TR': 'TRY', 'TM': 'TMT', 'TC': 'USD', 'TV': 'AUD', 'UG': 'UGX', 'UA': 'UAH', 'AE': 'AED', 'GB': 'GBP', 'UM': 'USD', 'US': 'USD', 'UY': 'UYW', 'UZ': 'UZS', 'VU': 'VUV', 'VE': 'VES', 'VN': 'VND', 'VG': 'USD', 'VI': 'USD', 'WF': 'XPF', 'EH': 'MAD', 'YE': 'YER', 'ZM': 'ZMW', 'ZW': 'ZWL'}
    banks = {
    "106": {'bank_name': 'HSBC', 'FX': {
        'EUR': 1.07,
        'USD': 1.14,
        'TRY': 21.24,
        'AUD': 1.62,
        'BD': 0.42,
        'BBD': 2.23,
        'AED': 4.11,
        'CHF': 1.01,
        'SEK': 11.43,
        'SGD': 1.47,
        'SAU': 4.12,
        'JPY': 152.80,
        'HKD': 8.78,
        'CNY': 7.62,
        'CAD': 1.54
    }},
    "074": {'bank_name': 'BARCLAYS', 'FX': {
        'EUR': 1.07,
        'USD': 1.14,
        'TRY': 20.63,
        'AUD': 1.64,
        'BD': 0.42,
        'BBD': 2.19,
        'AED': 4.14,
        'CHF': 1.05,
        'SEK': 11.88,
        'SGD': 1.51,
        'SAU': 4.24,
        'JPY': 153.81,
        'HKD': 8.93,
        'CNY': 7.47,
        'CAD': 1.52
    }}
    }
    currency = output["CURRENCY"]

    if bank in info and len(output["BAN"]) == 10:
        return 'The current exchange rate for GBP/' + currency + ' is  ' + str(banks[bank]['FX'][currency]) + '.'

    else:
        return "Invalid Bank Account Number. Please try again."


if __name__ == '__main__':
    app.run(debug=True, port=5000)
