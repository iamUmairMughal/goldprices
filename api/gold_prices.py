import re
import requests

Links= {
    'Australia': 'https://www.urdupoint.com/business/gold-rates-in-australia-AUD.html',
    'Canada': 'https://www.urdupoint.com/business/gold-rates-in-canada-CAD.html',
    'Japan': 'https://www.urdupoint.com/business/gold-rates-in-japan-JPY.html',
    'Pakistan': 'https://www.urdupoint.com/business/gold-rates-in-pakistan-PKR.html',
    'UAE': 'https://www.urdupoint.com/business/gold-rates-in-uae-AED.html',
    'UK': 'https://www.urdupoint.com/business/gold-rates-in-uk-GBP.html',
    'USA': 'https://www.urdupoint.com/business/gold-rates-in-usa-USD.html',
    'Afghanistan': 'https://www.urdupoint.com/business/gold-rates-in-afghanistan-AFN.html',
    'Albania': 'https://www.urdupoint.com/business/gold-rates-in-albania-ALL.html',
    'Algeria': 'https://www.urdupoint.com/business/gold-rates-in-algeria-DZD.html',
    'Argentina': 'https://www.urdupoint.com/business/gold-rates-in-argentina-ARS.html',
    'Bahamas': 'https://www.urdupoint.com/business/gold-rates-in-bahamas-BSD.html',
    'Bahrain': 'https://www.urdupoint.com/business/gold-rates-in-bahrain-BHD.html',
    'Bangladesh': 'https://www.urdupoint.com/business/gold-rates-in-bangladesh-BDT.html',
    'Barbados': 'https://www.urdupoint.com/business/gold-rates-in-barbados-BBD.html',
    'Bermuda': 'https://www.urdupoint.com/business/gold-rates-in-bermuda-BMD.html',
    'Brazil': 'https://www.urdupoint.com/business/gold-rates-in-brazil-BRL.html',
    'Bulgaria': 'https://www.urdupoint.com/business/gold-rates-in-bulgaria-BGN.html',
    'Chile': 'https://www.urdupoint.com/business/gold-rates-in-chile-CLP.html',
    'China': 'https://www.urdupoint.com/business/gold-rates-in-china-CNY.html',
    'Colombia': 'https://www.urdupoint.com/business/gold-rates-in-colombia-COP.html',
    'Costa Rica': 'https://www.urdupoint.com/business/gold-rates-in-costa-rica-CRC.html',
    'Croatia': 'https://www.urdupoint.com/business/gold-rates-in-croatia-HRK.html',
    'Czech Republic': 'https://www.urdupoint.com/business/gold-rates-in-czech-republic-CZK.html',
    'Denmark': 'https://www.urdupoint.com/business/gold-rates-in-denmark-DKK.html',
    'Dominican-republic': 'https://www.urdupoint.com/business/gold-rates-in-dominican-republic-DOP.html',
    'Egypt': 'https://www.urdupoint.com/business/gold-rates-in-egypt-EGP.html',
    'Estonia': 'https://www.urdupoint.com/business/gold-rates-in-estonia-EEK.html',
    'Fiji': 'https://www.urdupoint.com/business/gold-rates-in-fiji-FJD.html',
    'Hong Kong': 'https://www.urdupoint.com/business/gold-rates-in-hong-kong-HKD.html',
    'Hungary': 'https://www.urdupoint.com/business/gold-rates-in-hungary-HUF.html',
    'Iceland': 'https://www.urdupoint.com/business/gold-rates-in-iceland-ISK.html',
    'India': 'https://www.urdupoint.com/business/gold-rates-in-india-INR.html',
    'Indonesia': 'https://www.urdupoint.com/business/gold-rates-in-indonesia-IDR.html',
    'Iran': 'https://www.urdupoint.com/business/gold-rates-in-iran-IRR.html',
    'Iraq': 'https://www.urdupoint.com/business/gold-rates-in-iraq-IQD.html',
    # 'Israel': 'https://www.urdupoint.com/business/gold-rates-in-israel-ILS.html',
    'Jamaica': 'https://www.urdupoint.com/business/gold-rates-in-jamaica-JMD.html',
    'Kenya': 'https://www.urdupoint.com/business/gold-rates-in-kenya-KES.html',
    'Kuwait': 'https://www.urdupoint.com/business/gold-rates-in-kuwait-KWD.html',
    'Lebanon': 'https://www.urdupoint.com/business/gold-rates-in-lebanon-LBP.html',
    'Malaysia': 'https://www.urdupoint.com/business/gold-rates-in-malaysia-MYR.html',
    'Mauritius': 'https://www.urdupoint.com/business/gold-rates-in-mauritius-MUR.html',
    'Mexico': 'https://www.urdupoint.com/business/gold-rates-in-mexico-MXN.html',
    'Morocco': 'https://www.urdupoint.com/business/gold-rates-in-morocco-MAD.html',
    'New Zealand': 'https://www.urdupoint.com/business/gold-rates-in-new-zealand-NZD.html',
    'Norway': 'https://www.urdupoint.com/business/gold-rates-in-norway-NOK.html',
    'Oman': 'https://www.urdupoint.com/business/gold-rates-in-oman-OMR.html',
    'Peru': 'https://www.urdupoint.com/business/gold-rates-in-peru-PEN.html',
    'Philippines': 'https://www.urdupoint.com/business/gold-rates-in-philippines-PHP.html',
    'Poland': 'https://www.urdupoint.com/business/gold-rates-in-poland-PLN.html',
    'Qatar': 'https://www.urdupoint.com/business/gold-rates-in-qatar-QAR.html',
    'Romania': 'https://www.urdupoint.com/business/gold-rates-in-romania-RON.html',
    'Russia': 'https://www.urdupoint.com/business/gold-rates-in-russia-RUB.html',
    'Saudi Arabia': 'https://www.urdupoint.com/business/gold-rates-in-saudi-arabia-SAR.html',
    'Singapore': 'https://www.urdupoint.com/business/gold-rates-in-singapore-SGD.html',
    'Slovakia': 'https://www.urdupoint.com/business/gold-rates-in-slovakia-SKK.html',
    'South Africa': 'https://www.urdupoint.com/business/gold-rates-in-south-africa-ZAR.html',
    'South Korea': 'https://www.urdupoint.com/business/gold-rates-in-south-korea-KRW.html',
    'Sri Lanka': 'https://www.urdupoint.com/business/gold-rates-in-sri-lanka-LKR.html',
    'Sudan': 'https://www.urdupoint.com/business/gold-rates-in-sudan-SDG.html',
    'Sweden': 'https://www.urdupoint.com/business/gold-rates-in-sweden-SEK.html',
    'Switzerland': 'https://www.urdupoint.com/business/gold-rates-in-switzerland-CHF.html',
    'Thailand': 'https://www.urdupoint.com/business/gold-rates-in-thailand-THB.html',
    'Trinidad and Tobago': 'https://www.urdupoint.com/business/gold-rates-in-trinidad-and-tobago-TTD.html',
    'Tunisia': 'https://www.urdupoint.com/business/gold-rates-in-tunisia-TND.html',
    'Turkey': 'https://www.urdupoint.com/business/gold-rates-in-turkey-TRY.html',
    'Venezuela': 'https://www.urdupoint.com/business/gold-rates-in-venezuela-VEF.html',
    'Vietnam': 'https://www.urdupoint.com/business/gold-rates-in-vietnam-VND.html',
    'Zambia': 'https://www.urdupoint.com/business/gold-rates-in-zambia-ZMK.html',
    }

scale = {
    'tola' : '24k per Tola',
    'grams' : '24k 10g'
}

def find_price(c, s):
    api =''
    ur =''
    api = Links.get(c)
    sl = scale.get(s)
    try:
        ur = requests.get(api)
    except:
        return 'ERROR'

    html = ur.text
    str_to_Search = f'data-label="{sl}"'
    str1 = re.search(str_to_Search, html, re.I)
    if str1:
        index_val = html.index(str_to_Search)
        index_val_update = index_val + len(str_to_Search) + 4
        index_val_update_end = index_val + 38
        price = html[index_val_update:index_val_update_end]
        price = re.sub(r'<+/*\w*', '', price)
        price = price[1:]
        return str(price)
    else:
        return 'NULL'

print(find_price('Pakistan', 'tola'))