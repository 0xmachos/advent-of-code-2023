#!/usr/bin/env python3
# advent-of-code-2023/dec1.py

# On each line, the calibration value can be found by combining the first digit
# and the last digit (in that order) to form a single two-digit number.

import re
input = open("dec1-input.txt", 'r')

numbers_to_sum = []

for line in input:
    numbers = re.findall(r'\d', line)
    # Find every digit on each line
    # This produces a list of digits e.g. ['6', '7', '2']
    calibration_value = numbers[0] + numbers[-1]
    # Concatenate the first and last number in the list
    # We can use + since we are dealing with strings
    numbers_to_sum.append(int(calibration_value))
    # Cast the new number e.g. 62 to int and add it to a list

print(sum(numbers_to_sum))
# Answer is: 54667


# Your calculation isn't quite right. It looks like some of the digits are actually spelled
# out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".
# Equipped with this new information, you now need to find the real first and last digit on each line.
input = open("dec1-input.txt", 'r')

numbers_to_sum = []
for line in input:

    line = re.sub("(.*?)one(.*?)", r'\1one1one\2', line)
    line = re.sub("(.*?)two(.*?)", r'\1two2two\2', line)
    line = re.sub("(.*?)three(.*?)", r'\1three3three\2', line)
    line = re.sub("(.*?)four(.*?)", r'\1four4four\2', line)
    line = re.sub("(.*?)five(.*?)", r'\1five5five\2', line)
    line = re.sub("(.*?)six(.*?)", r'\1six6six\2', line)
    line = re.sub("(.*?)seven(.*?)", r'\1seven7seven\2', line)
    line = re.sub("(.*?)eight(.*?)", r'\1eight8eight\2', line)
    line = re.sub("(.*?)nine(.*?)", r'\1nine9nine\2', line)
    # For every number word (e.g. six) add the actual number six (6) after it followed by the number word
    #   Note: Unclear why you need to use number_word/number/number_word. I copied Stefan via CyberChef for this
    #     https://gchq.github.io/CyberChef/#recipe=Find_/_Replace(%7B'option':'Regex','string':'(.*?)one(.*?)'%7D,'$1one1one$2',true,false,true,false)Find_/_Replace(%7B'option':'Regex','string':'(.*?)two(.*?)'%7D,'$1two2two$2',true,false,true,false)Find_/_Replace(%7B'option':'Regex','string':'(.*?)three(.*?)'%7D,'$1three3three$2',true,false,true,false)Find_/_Replace(%7B'option':'Regex','string':'(.*?)four(.*?)'%7D,'$1four4four$2',true,false,true,false)Find_/_Replace(%7B'option':'Regex','string':'(.*?)five(.*?)'%7D,'$1five5five$2',true,false,true,false)Find_/_Replace(%7B'option':'Regex','string':'(.*?)six(.*?)'%7D,'$1six6six$2',true,false,true,false)Find_/_Replace(%7B'option':'Regex','string':'(.*?)seven(.*?)'%7D,'$1seven7seven$2',true,false,true,false)Find_/_Replace(%7B'option':'Regex','string':'(.*?)eight(.*?)'%7D,'$1eight8eight$2',true,false,true,false)Find_/_Replace(%7B'option':'Regex','string':'(.*?)nine(.*?)'%7D,'$1nine9nine$2',true,false,true,false)Find_/_Replace(%7B'option':'Regex','string':'(.*)zero(.*)'%7D,'$1zero0zero$2',true,false,true,false/disabled)Find_/_Replace(%7B'option':'Regex','string':'%5B%5E%5C%5Cd%5C%5Cn%5D'%7D,'',true,false,true,false)Find_/_Replace(%7B'option':'Regex','string':'(%5E%5C%5Cd).*(%5C%5Cd$)'%7D,'$1$2',true,false,true,false)Find_/_Replace(%7B'option':'Regex','string':'%5E(%5C%5Cd)$'%7D,'$1$1',true,false,true,false)Sum('Line%20feed')&input=ZHFmb3VybmluZTVmb3VyMmptbHFjZ3YKN2dnemRuanhuZGZpdmUKdHdvZml2ZTR0aHJlZW5pbmUKZHR0d29uZXpiZ21jc2V2ZW41c2V2ZW4KNXZzcmNuaW5lCjk1enpiamNrCmdrb25laWdodDRmaXZla3ZrdGx0bmluZQpmaXZlcmNrZG1nYmZ0aGpkcXBtcGdka21ja2xxdHFjMzY1bXF0d28KNDRzZXZlbmh2c3RjYmdraG01Zm91cmVpZ2h0MTEKZHBycnRybmdyZmNjejRlaWdodDR0d284c3RobWZpdmUKNnR3b2ZpdmU0c2V2ZW43bmluZQpmb3VyMXNldmVuYmZibnF2a2Jmb3Vyc2l4NwoxMnhwZGdocGVpZ2h0cXZ6dHJzc2xnc2l4NXNtbGdmamhjcHN0CjhkaHpkdGJlaWdodGZvdXIzCnB0dGR0bWhnNAo2ZWlnaHRzZXZlbmRidGJ4bnF6eGRzNgp0d290aHJlZTVueGdscWxjOQpuaW5lNmxxaG52YnB4b25lc2V2ZW5laWdodHN4amZrejR2cgp0aHJlZTI4anhkbWxxZm1jNjE5ZWlnaHR3b2wKMjZqdGRwZ3FqenNobmN4dmxsamZvdXIKcXh2cHNjdGd4MQoyODI4NnFkampsZ3RkdG5zbTNoawo5aGNqNm5pbmUKbmluZXNldmVuOXNxdHJwZm91cgpvbmUxZWlnaHQ0c2l4emx0enJrdGhyZWUKdGhyZWV2bGdmeGhuZjZzZXZlbjZuaW5lNjgKc2l4b25lc3h4Ynh2Zm5rdDgKOGZpdmVmaXZlZm91cjdzeHNydmRyegpvbmVvbmU3Cm5kdGtqYnNpeDZ0aHJlZTlnZHNqbGxqdGo2c2l4CmNmbXJmZ2pxZ3J6Y21zaXg1CjN0aHJlZWZvdXI2MnRocmVlM3ZybW5tZ3gKa2NrZGdoc2V2ZW50d28xNzU4Cm1kYnFxam1wdm9uZXR3bzFzaXgzMWZvdXJudGJmYgpsa2poamR0aHJlZTMKcXRoc2V2ZW42MW1wZm5uaG02Zml2ZWNuaHoyCnR3b2pyZmd6anN0anZsbmducHFjajhncnRudnhtemJ4a2ZydnFtdm5tdm1iZHIKc2xvbmVpZ2h0a3FiZ2NwbnY4a3FjbXpmb3Vyb25lc2V2ZW5tcmZqZWlnaHQKeGR4ZHhnOXNldmVudHdvOHhjcTEKZHBkZ3h6azcKMThzaXgzdHdvb25lCjF0d29zZXZlbjNmaXZlCjQ2dGtiY2xia2xlaWdodDY0CnRqcHJwamJzaHIyc2V2ZW4xcGdmcW1ibWpsdnN2CjNtYmpjY3Nzamd0ZHR0dmJkaGRmeHZsZHBtaGNwYwpsZ2Zya3BzZnZ6NXBwZ3FwaHR3b3puanRneGRqcG0zCm1qbWxzZXZlbmdnc2JqYnRzaXg5bmluZW9uZQpqcWZxanFodGhyZWVuaW5lN2VpZ2h0a2xrdHRka2J0bXBwMQp0cnB0cmtib25lNTJlaWdodDYKb25ldG12c3JqbGJxbG5pbmVzaXg4CnJvbmU5a3R2ZHFrZGdsMQp0d29zaXg1c2l4Z3JmZGZ0NTRrbGY0CnRocm1vbmUzZWlnaHRzaXhmaXZlCnRocmVlNG9uZQpwcHRoZzJ0aHJlZTFvbmUKN3Z0NDI2CjIyZm91cmVpZ2h0Ngpmb3VyeGJobW9uZTU2c2V2ZW44ZWlnaHRuaW5lCnZobXNkMTcxcmdraHBnZmhmZm5oa3Z0CnhnYnp4c3pzZ3R0aHJlZTQKcmNsemZzbjV0d29laWdodAo5ODluaW5lMnNldmVuCmVpZ2h0ZWlnaHQ1Zml2ZW5zaXg4CmRmeHp6NXFjcXpzanNnCmQzZWlnaHQ1NAo1a25mbGhudHp0aHJlZXNldmVudHdvCnRocmVlb25lZm91cjlvbmVuaW5lYnNmcHEKaGpoZ3RqZ3R3b3Ryc2ZmaXZlOGhmbnRtCnNpeHBtaHpxcmxrcnRocmVlZm91cjFwY2d2ejk2CjV0aHJlZTMxeHFjc3Noa2txdGZibGZmY21jbnRmb3VyCnpnaGNmdmpzZnoyOW5pbmUKM3Z2dnJscmpkenRsaHFxbTg4CjM5bmluZTNzZXZlbjkzCjFmcXNnbmp6cmw2bHJ6c2N6Ywp0aHJlZXBsZHp0bG52bnpkbnRxbGxwcjE5Cm5pbmVrZ3Fxcmd0dGZudHJoanpsdm5pbmVscjMKOTRlaWdodGVpZ2h0ZWlnaHQKdHdvMTN0eG10bHF4c2tobHRrcnZianJ6bTk3Zml2ZQpkYm1qdnN6anRiMTcKdHdvZ3BmdHRtaHA4dHdvMTMKZm91cjRicXpxc2NkYmN0c3NneGZ6ampudHdvbmZja3RqcnRueHNranBraHZsZmp0CmN0eHh2ZHN2c3ZqemNobXh2eGNlaWdodHRocmVlbWJubGc1bmluZXZtY2Jnc3ZiaApmcGJycGZvdXJxbXJmY25wdnhnOG9uZWhrYmJnYnNubnQKNHpycmdzZXZlbmZvdXIKNmVpZ2h0OWZvdXJlaWdodHhsZ2RuCjY5M3J6Y252bGZydgpiY2Z0bnRjZmw0anhiY2NwY21qZWlnaHRjcnhzanNjbXhkZWlnaHRtaHFibnBkdmNmb3VyCnNpeDgzCnhsNApuanNsY2tjYmRmdmtta2RrOWVpZ2h0Cm5pbm
    # (.*?) are (lazy) capture groups that capture everything before and after the number word
    # We replace these back into the new string to preserve the original string contents
    # Original: 5six3four9nine8
    # Modified: 5six6six3four4four9nine9nine8
    numbers = re.findall(r'\d', line)
    # Find every digit on each line
    # This produces a list of digits e.g. ['5', '3', '9', '8']

    numbers_to_sum.append(int(numbers[0] + numbers[-1]))
    # Build a new number using the first and last numbers in the list and cast the new number e.g. 58 to int
    # then add it to a list

print(sum(numbers_to_sum))
#  Answer is: 54203
