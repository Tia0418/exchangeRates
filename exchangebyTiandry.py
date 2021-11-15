import requests

url = 'http://api.exchangeratesapi.io/v1/2010-01-15?access_key=cf58f4b4a3bf48eff4455b1c08bd3b12&base=EUR'

response = requests.get(url)
data = response.json()

rates = data.get('rates')
print(rates)

with open("file.html","w") as file:
    file.write( 
    """ <table>
    <tr>
    <th>Currency</th>
    <th>Exchange rate (base EUR)</th>
    </tr>\n""")
    for i in rates:
        file.write("<tr>\n<td>"+i+"</td>\n<td>"+str(rates[i])+"</td>\n</tr>\n")
    file.write("</table>\n")
    file.close()
         
    

    
