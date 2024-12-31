import speech_commands as sp
from ubinascii import a2b_base64, b2a_base64

data = a2b_base64('BAgJAQoiBvPyEegEFenTws3zENMrFPPR8Rry5CzQKrvz+RMHHtjK9wPgKPMG/Bb6HNL3Aufe7eLz4yn6HfUFvczaBuw7CRX8Es8OySPq9Qoa3y0K9ATs/w/pIgn16OD6ACEV8AcBCsX62BHkDP75+PPhG+IuziLk7eEk+iD8/Qkj9APfBsrv6vHgEQEg9tXn4hsV6C37AxXz9RH8EeXsAwPkBgPaEdn7Ef8h4/vu3ekR2hAE7Owk7fAN+/kVF9rx9gMK8fgl8P0N6Az3Gv4HB7zl6PAkKfHYAQXuEAcOE/n/6QPvAfbs7wPbM/Do8xEl/dQK//b/DRjPB+j7FAHXDwr69AbyBybM8vHpJPnc4PDl5yzwHhTr0vYmAdIJzg7aCusI+vTv5QkD8BTh+OMN+hno+QEEz/r/4M0u+RsL+K/IxxH1G/AWzuIG9dod8/0b//gMAvL98vgb3xgM4fH8E/gH9too5QwD9+ws8Qr/0cff1S/uMgvZ7wfqBOsAAiEBD9P7/eEb2vTmzu38F+wY0/cc5v1AAw4C+gfg2iDL+ykExRPk6CLwACzl4O7zJfkTGgL6+Ob7AuYV9OsPCQT57Ob9+wb47+nt+fYDEg4IFAq/CuIAGBnZIB8H6OcJAgH9AeYO/gf/5e/t7CIp4w78Df31+gXtCf7v2Prr/PD5E/gREgLo6ggJESYP4Bns5ePd9+8f+C8D7NHsDg3mOdEI7PEFCP8kwd8g+eQO2eH1+AsG9xQJ9P0bBNPZBwYYIP3I8s//2wob9eck//bz+ubq/g8NExbq1/IEIwwAz/L57Pv6CufeB+gsDgncJfQD3wPG4/P++x37+RIK0hH++hb5BQDkCtj1/v4Q0fr3GAL549nb5SrXFwzhFOnX5dAZ3P0NBe8bBeMBAwcO6gj68AYKFiv63P/bBv3g+gzd5iTr7xnm/f376/cO7BIE5wnV/hsT/eT19isBEAECHPHaBOIQBhLr7+gJ/OIABwIdBwLo9/vyA/EM3QkQAsDn8eYWDAr+FgAU4t4KGPAKL/cO9uPm3+f8IfMUJN3nyQHx0iDW7xDo/Tj77uLsEevYJxf9IfUREhzgBvzY4PDQ6BcACvwK/vL1/eURFe3s9Pfu+SkP88X34BEkFwIN9w4fDfbxEtz4CQTx4P7b/Cf49Bjn9dYZEdERAfgW89/rDsERDgvwKCMV0hfW5ise+uUW5fIi5One/A8WyjkV3gkW//3NGdboCwX7NuzzFBX7D+Tw1QD4CjMD/AH21PQI0wH/8vEfD/EE9fAV9vMD6dkC+e4CCfkj7uv6BsYm/gT9Dvjp9Bb0BvgTAATyBfjaEhgBHRXR5BEaChjvJM8K/xXuIgYB9vre6hbwCN8K3gDpHRv0BP7m6uzUAhDXNg338en84csZzf8RA/Hx//fjzA763i342/YGEQEH9PTt8gj3/vgwBBcJDQb4BebPHQUP3AwU5RMdDQ8WF9jtG/XIB+wXD/zpAAfF5h31/eb11A4b6AYD2ucEFeADDwLxGRLgFQvf8wXpDRYVBO/74NgCHBHkFPT3DfH0+An47uIgGsAN/ebv/QDC3/cD5Rr9FBUT6g/62ev+/PsDDAYD8PrMEOndEQT2DwoB+wIA7NXw/+7a7PL1AAf7KCXF6wrkIOcU+iEW3NkD5A/IHP/29PD2CuoMAAIODOwyDxH34hf13h78+AABCxIb9f7k6iTmBePy7A4p+PPv9NzUzSMU0SUK3ev2APDuK9MUGvrkEAfy1fwXDtI1FfQEFwr9Asfr7O77+xfeEusVBgUHEAvv6Bb2+N4BBvUP+/cH//7QIAn27grvGwQI8AD+4PASIwLy9eUa+vgO8+YIChDb9/kEBO4q7xv/3gEe6tgxCQbrCeL1/RoqBgDiDfjd99Pf+iTiERnaAvD3B/b/2e8GG+ULAwQEAxQg6wQE6PwMJATlDf/k9Q4f9BT77esXBwrl/PTXGyAC2/Do/PQLFxwB1eDc3f/eCBu89ATkEvXy9jIAAu31CPID+AgXH/n0FPoEEOIj/fb6E+kC6f4R8hz7+PDh6+7+HtoSGdkM387ez9ERC8wz3fr94ysNwh77BRP2/v/wDPHfBxntFAHpGQEBFCH04+X9/Ofu6QX4DC/l9gT3ANUOFPPv2yjuABUCBcwE0wAV+OwQ7vgYAMoO/dP/Kfr6Bva+FAEI9uDk6f0c1+T+7gIiHxr58On28vHcKiUQxs/L4w78DdkL8AkO//zsuA0T3Rsx1Qnu+QwFD+Ln9QbyHhji4fzy/vD6/f/49h/2+gjj+Occ8e8I2fT18hYC2wvi2TML+eX7Gd4LDw4YEtbxB9gPI8wA1O/7DBcO8gwlHPjg5AHsCvb9CBf07xQODiz3C/D0Fh3v5gwe6/z3+BXiF/3s+v7x5xfY8ADn2rHwFwrJIuLN6Ocf+uIi+ebp//0L7wrz3Ajr1R349BkY6Er9yt3t/PXN19saBBsN+BkC+ujgGRXq7Or75hQC8RDqA+UpDwjeDeYs6w3oFwHO4g8RCwv37gIa4fkT+PL8IuT8DATzIwobDfLv8A/b5SQqGNz1yf0A3xK+EPv+CN7qzu79JeE9KckNy9/o8ybb5wkV1iD64+Xz8x0SDQUG+O0rAtcX89ceAfTV+eMi/QMWFez+4uIH6vbl5AUSHgoA//3bC83fCQsRDs/2Av4IAhDTEB7f8QXx9wfrCPIz990D9/4T7xwG+vcN8v3wFxzzA+H03QQDF+cQ2e4T1QQM6efWxBoKzyK/7g/LJwnpMfvt9QHqGwHzBcgK3e886g8e/f4S+vQD3PkD5ArbK90eERcCDgLp0gn38dEGIf0U7eoT3d/QHBsSxhIUFgf19fQNyuYyH/X97McONuz4Ce7s4SQR6t0S8AcG+irT3PUTxPcmAAvQ5s0V+xP/w+P1BxLn5+ft5RrUIyW/ENn06QAD5e+xGuoWBuD39QgB+w/w8QbwJ+nn+NfaAe4SxhDxGPfwDR8FCN3f0/r/7fr50wPnByYD2hLt2AkQBfYH8RzmGCgXA+0ewt0p/dLy+/UHE+7CDQwYC/wR0hYUAA/55An1E9YS/PEqBwLAm7Bk')
sp.init(data)
labels = ["Berhenti","Wakeword","Mulai","[OTHER]"]
feature = bytearray(732)

def predict(audio):
    result = sp.predict(audio, 0, 0)
    return (labels[result // 1000], result % 1000)

def snapshot():
    global feature
    sp.export_mfcc(feature)

def save(label):
    with open('samples.txt', 'ab') as f:
        f.write(b'{"label": "')
        f.write(label.encode())
        f.write(b'", "mfcc": "')
        f.write(b2a_base64(feature)[:-1])
        f.write(b'"},\n')
