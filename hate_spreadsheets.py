import requests
import datetime as dt
import time
import mysql.connector


## DB CONNECT
mydb = mysql.connector.connect(
  host="",
  user="",
  password="",
  database=""
)

inicio = time.strftime('%H:%M:%S')
start_dt = dt.datetime.strptime(inicio, '%H:%M:%S')
print ('[i] Início: %s' % time.strftime('%H:%M:%S'))

sistemas = ['https://www.semas.pa.gov.br/agendamento/','http://sistemas.semas.pa.gov.br/cbpa/login','http://catis.semas.pa.gov.br/','https://www.semas.pa.gov.br/tfrh','http://sistemas.semas.pa.gov.br/dashboardAlertas/#/','https://falabr.cgu.gov.br/publico/PA/Manifestacao/RegistrarManifestacao','http://sistemas.semas.pa.gov.br/entradaUnica/portalSeguranca/#/','http://sistemas.semas.pa.gov.br/fiscalizacao/login','http://sistemas.semas.pa.gov.br/gestaoDemandas/#/login','https://www.semas.pa.gov.br/hidromet','https://monitoramento.semas.pa.gov.br/ldi/','https://www.semas.pa.gov.br/legislacao','http://sistemas.semas.pa.gov.br/portalSeguranca/#/','http://sistemas.semas.pa.gov.br/entradaUnica/portalSeguranca/#/','http://sistemas.semas.pa.gov.br/pra/validacao-documentos/#/','https://monitoramento.semas.pa.gov.br/monitoramento/#/sig','http://sistemas.semas.pa.gov.br/pra/consultaPublica','https://www.semas.pa.gov.br/semanet','http://monitoramento.semas.pa.gov.br/seirh/#/Inicio/','http://car.semas.pa.gov.br','http://sistemas.semas.pa.gov.br/sigerhpa','http://monitoramento.semas.pa.gov.br/simlam/index.htm','http://monitoramento.semas.pa.gov.br/auditoria/','https://monitoramento.semas.pa.gov.br/sisflora2/sisflora.app/#/home','http://sistemas.semas.pa.gov.br/sisflora/login','https://www.semas.pa.gov.br','http://www.municipiosverdes.pa.gov.br','http://sistemas.semas.pa.gov.br/sisfap/login','http://www.semas.pa.gov.br:8083/gdg/','http://bi.semas.pa.gov.br/Reports','https://www.semas.pa.gov.br/dapp','https://www.semas.pa.gov.br/compensacao2']

result = []

for i in range (len(sistemas)):
    #print(sistemas[i])
    try:
        res = requests.get(sistemas[i])
    except:
        result.append('NOK')

    if(res.status_code in (200,401)):
        #result.append(res.status_code)
        result.append('OK')
        #print(res.status_code)
    else:
        result.append('NOK')
        #print(res.status_code)

fim = time.strftime('%H:%M:%S')
end_dt = dt.datetime.strptime(fim, '%H:%M:%S')
diff = (end_dt - start_dt) 
diff.seconds/60 

mycursor = mydb.cursor()

sql = "INSERT INTO disponibilidade (agendamento,cbpa,catis,cerh,dashboard,denuncias,entrada_unica,fiscalizacao,gestao_demandas,hidromet,ldi,legisemas,licenciamento_simplificado,modulo_relatorios,modulo_juridico,monitoramento,pra,semanet,seirh,sicar,sigerhpa,simlam,sisflora1,sisflora2,sisflora_relatorios,site_semas,nepmv,sisfap,gdga,bi,sc2a,dapp) VALUES ('"+result[0]+"','"+result[1]+"','"+result[2]+"','"+result[3]+"','"+result[4]+"','"+result[5]+"','"+result[6]+"','"+result[7]+"','"+result[8]+"','"+result[9]+"','"+result[10]+"','"+result[11]+"','"+result[12]+"','"+result[13]+"','"+result[14]+"','"+result[15]+"','"+result[16]+"','"+result[17]+"','"+result[18]+"','"+result[19]+"','"+result[20]+"','"+result[21]+"','"+result[22]+"','"+result[23]+"','"+result[24]+"','"+result[25]+"','"+result[26]+"','"+result[27]+"','"+result[28]+"','"+result[29]+"','"+result[30]+"','"+result[31]+"')"

mycursor.execute(sql)
mydb.commit()

print('\nSALVO NO BANCO')

#print(sql)

#print("#####################################################\n")
#print(result)
#print("#####################################################\n")
print ('\n[i] Término: %s' % time.strftime('%H:%M:%S'))
print ('Tempo de execução: ',diff)
#print(diff)
