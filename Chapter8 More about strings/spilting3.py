def main():
    evc = '*712*619355938*51#'
    # evc = evc.lstrip('*')
    print(evc)
    evc_list = evc.split('*')
    number = evc_list[2]
    blance = evc_list[3]
    print('ma hubtaa in aad $',blance.rstrip('#'),'u direysid lambar-ka ',number, '?')
    print('1. Haa\n2. Maya')
    user = input('')
    if user == '1':
        print('Waxaaad $',blance.rstrip('#'),'dollar aa u dirtay lamber-ka ',number, '.\nHaraagaagu hadda waa $...')
    else:
        print('Waad ku guuleysatay in aad istaajisid ')
main()