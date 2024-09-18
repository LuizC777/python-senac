tenho_sede=False
tenho_fome=True

if tenho_sede and tenho_fome:
    print('fazer um saunduiche e um suco')
elif tenho_sede and not (tenho_fome):
    print('tomar suco')
elif not(tenho_sede) and tenho_fome:
    print('fazer um sanduiche')
else:
    print('ficar de boas')