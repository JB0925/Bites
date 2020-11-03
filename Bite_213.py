import re


bite_15_en = '''<p>Iterate over the given <code>names</code> and <code>countries list</code>s, <strong>printing</strong> them prepending the number of the loop (starting at 1). Here is the output you need to deliver:<pre>
1. Julian     Australia
2. Bob        Spain
3. PyBites    Global
4. Dante      Argentina
5. Martin     USA
6. Rodolfo    Mexico
</pre></p><p>Notice that the 2nd column should have a fixed width of 11 chars, so between <i>Julian</i> and <i>Australia</i> there are 5 spaces, between <i>Bob</i> and <i>Spain</i>, there are 8. This column should also be aligned to the left.</p><p>Ideally you use only one for loop, but that is not a requirement.</p><p>Good luck and keep calm and code in Python!</p>'''
bite_15_it = '''<p>Iterare i <code>nomi</code> e le <code>liste dei paesi</code>s indicati, <strong>stampandoli</strong> anteponendo il numero del ciclo (a partire da 1). Ecco l'output che devi consegnare:<pre> 1. Julian Australia 2. Bob Spagna 3. PyBites Global 4. Dante Argentina 5. Martin Stati Uniti d'America 6. Rodolfo Messico </pre></p><p>Si noti che la seconda colonna dovrebbe avere una larghezza fissa di 11 caratteri, quindi tra <i>Julian</i> e <i>Australia</i> ci sono 5 spazi, tra <i>Bob</i> e <i>Spagna</i> , ci sono 8. Questa colonna dovrebbe anche essere allineata a sinistra. </p><p>Idealmente si utilizza solo uno for loop, ma questo non è un requisito. </p><p>Buona fortuna e mantenere la calma e codice in Python! </p>'''
bite_15_it_fixed = '''<p>Iterare i <code>names</code> e le <code>countries list</code>s indicati, <strong>stampandoli</strong> anteponendo il numero del ciclo (a partire da 1). Ecco l'output che devi consegnare:<pre>
1. Julian     Australia
2. Bob        Spain
3. PyBites    Global
4. Dante      Argentina
5. Martin     USA
6. Rodolfo    Mexico
</pre></p><p>Si noti che la seconda colonna dovrebbe avere una larghezza fissa di 11 caratteri, quindi tra <i>Julian</i> e <i>Australia</i> ci sono 5 spazi, tra <i>Bob</i> e <i>Spagna</i> , ci sono 8. Questa colonna dovrebbe anche essere allineata a sinistra. </p><p>Idealmente si utilizza solo uno for loop, ma questo non è un requisito. </p><p>Buona fortuna e mantenere la calma e codice in Python! </p>'''





def fix_translation(org_text=bite_15_en, trans_text=bite_15_it):
    """Receives original English text as well as text returned by translator.
       Parse trans_text restoring the original (English) code (wrapped inside
       code and pre tags) into it. Return the fixed translation str
    """
    pre_corrections = re.findall(r'<pre>[A-Za-z0-9\s\.]+</pre>',org_text)
    pre_corrections = ' '.join(pre_corrections)
    code_corrections = re.findall(r'<code>[a-zA-Z0-9\s]+</code>',org_text)
    t_text = re.sub(r'<pre>\s[a-zA-Z0-9\.\s]+[\w\W]+?</pre>',pre_corrections,trans_text)
    trans_text_code_subs = re.findall(r'<code>[a-zA-Z0-9\s]+</code>',t_text)

    i = 0
    for item in trans_text_code_subs:
        if item in t_text:
            t_text = t_text.replace(item, code_corrections[i])
        i += 1
    
    return t_text == bite_15_it_fixed

    #print('t_text:\n\n\n')
    #print(t_text)
    #print()
    #print('expected:\n\n')
    #print(bite_15_it_fixed)
    



print(fix_translation())