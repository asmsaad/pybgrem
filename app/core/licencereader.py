import hmac
import hashlib
from datetime import datetime



def convert_and_validate_date(input_date):
    try:
        # Convert input date string to datetime object
        date_obj = datetime.strptime(input_date, '%d/%m/%Y')

        # Check if the date is valid
        if date_obj.year < 1000 or date_obj.year > 9999:
            return None

        # Format the date as DDMMYYYY
        formatted_date = date_obj.strftime('%d%m%Y')

        return formatted_date
    except ValueError:
        return None
    
def generaor(expaire_date,serial_number):
    # Secret key
    secret_key = b'*#%$!&'
    # Message
    message = b'@#$~~@#$'

    expaire_date  = str(convert_and_validate_date(str(expaire_date).strip()))
    serial_number = str(serial_number).strip()
    if len(serial_number)<8: serial_number = serial_number.rjust(8,'0')

    message_ = f'{expaire_date}_{serial_number}'

    # Calculate HMAC-SHA256 hash
    hmac_hash = hmac.new(secret_key, message, hashlib.sha1).hexdigest()
    print(hmac_hash)

    generatd_key = ''
    par_four = ''
    count = 0
    for index,character in enumerate(hmac_hash[:32]):
        index = index+1
        par_four += character
        if (index) % 4 == 0 and (index != len(hmac_hash)):
            generatd_key += message_.split('_')[0][count]+par_four +message_.split('_')[1][count]
            if index != 32 :
                generatd_key +=  '-'
            par_four = ''
            count += 1
    print('>>',generatd_key.upper())


    return generatd_key.upper()





    #todo reconstraction
def reconstract_licence(generatd_key):
    # Secret key
    secret_key = b'*#%$!&'
    # Message
    message = b'@#$~~@#$'


    date = ''
    serial = ''
    hash_val = ''

    reconst = generatd_key.lower().split('-')
    for each_segment in reconst:
        date += each_segment[0]
        serial += each_segment[-1]
        hash_val += each_segment[1:-1]


    print(date)
    print(serial)
    print(hash_val)
        
    provided_hmac_hash = hash_val
    calculated_hmac_hash = hmac.new(secret_key, message, hashlib.sha1).hexdigest()[:32]
    if provided_hmac_hash == calculated_hmac_hash:
        print("Message is authentic.")
    else:
        print("Message is not authentic.")


generatd_key = generaor('30/12/2024','56')
reconstract_licence(generatd_key)