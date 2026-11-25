from pyscript import document

def candidate_checker(e):
    club_members = ["jack sabitsana" , "kaizen sy" , "arturo santos" , "lucas sarte" , "hans ulit"]
    f_name = document.getElementById('first_name').value
    l_name = document.getElementById('last_name').value
    candidate = f_name + ' ' + l_name
    
    member_checker = candidate.lower() in club_members
    messages= (f'Sorry {candidate}, you are not on the baller list!',
               f'congratulatories! {candidate}, you are apart of the basketball varsity!')
    
    document.getElementById('result').innerHTML = messages[member_checker]