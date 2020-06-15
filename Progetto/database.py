from sqlalchemy import create_engine,MetaData,Table,Column,String,Integer,ForeignKey,DateTime,Float,Boolean,CheckConstraint,select,and_,PrimaryKeyConstraint,bindparam
from datetime import datetime
#from exceptions import EmptyResultException
class EmptyResultException(Exception):
    pass

class ResultException(Exception):
    pass
######################
engine=create_engine("postgres://enrico:alessandro@localhost:5432/cinema")
metadata=MetaData()
utenti=Table("Utenti",metadata,Column("email",String,primary_key=True)
                              ,Column("nomeUtente",String,nullable=False)
                              ,Column("pwd",String,nullable=False)
                              ,Column("annoNascita",Integer)
                              ,Column("sesso",String,CheckConstraint("sesso='M' OR sesso='F'"))
                              ,Column("provincia",String)
                              ,Column("gestore",Boolean,nullable=False)
                              ,Column("annoAssunzione",Integer))
film=Table("Film",metadata,Column("idFilm",Integer,primary_key=True)
                          ,Column("titolo",String,nullable=False)
                          ,Column("anno",Integer,CheckConstraint("anno>=1970"),nullable=False)
                          ,Column("regista",String,nullable=False)
                          ,Column("minuti",Integer,CheckConstraint("minuti>=1"),nullable=False))
generi=Table("GeneriFilm",metadata,Column("genere",String)
                                  ,Column("film",Integer,ForeignKey("Film.idFilm"),nullable=False)
                                  ,PrimaryKeyConstraint("genere","film"))
sale=Table("Sale",metadata,Column("idSala",Integer,primary_key=True)
                          ,Column("numPosti",Integer,CheckConstraint("\"numPosti\">=10"),nullable=False)
                          ,Column("disponibile",Boolean,nullable=False))
proiezioni=Table("Proiezioni",metadata,Column("idProiezione",Integer,primary_key=True)
                                      ,Column("orario",DateTime,CheckConstraint("orario >= '1970-01-01'::date"),nullable=False)
                                      ,Column("prezzo",Float,CheckConstraint("prezzo>=0.0"),nullable=False)
                                      ,Column("film",Integer,ForeignKey("Film.idFilm"),nullable=False)
                                      ,Column("sala",Integer,ForeignKey("Sale.idSala"),nullable=False))
biglietti=Table("Biglietti",metadata,Column("posto",Integer,CheckConstraint("posto>=0"),nullable=False)
                                    ,Column("proiezione",Integer,ForeignKey("Proiezioni.idProiezione"),nullable=False)
                                    ,Column("cliente",String,ForeignKey("Utenti.email"),nullable=False)
                                    ,PrimaryKeyConstraint("posto","proiezione"))


metadata.create_all(engine)

#conn=engine.connect()
#ins=utenti.insert()
#res=conn.execute(select([utenti]))
#for r in res.fetchall():
#    print(r)
#conn.execute(ins,{"email":"pittinienrico@hotmail.it","nomeUtente":"Enrico","pwd":"tarallo99","annoNascita":1999,"sesso":"M","provincia":"Treviso","gestore":False})
#ins=film.insert()
#conn.execute(ins,[{"idFilm":1,"titolo":"Memento","anno":2000,"regista":"Christopher Nolan","minuti":114},
#                  {"idFilm":2,"titolo":"Inception","anno":2010,"regista":"Christopher Nolan","minuti":148},
#                  {"idFilm":3,"titolo":"Insomnia","anno":2002,"regista":"Christopher Nolan","minuti":118},
#                  {"idFilm":4,"titolo":"The Prestige","anno":2006,"regista":"Christopher Nolan","minuti":130},
#                  {"idFilm":5,"titolo":"Una notte da leoni","anno":2009,"regista":"Todd Phillips","minuti":108},
#                  {"idFilm":6,"titolo":"Una notte da leoni 2","anno":2011,"regista":"Todd Phillips","minuti":102},
#                  {"idFilm":7,"titolo":"Una notte da leoni 3","anno":2013,"regista":"Todd Phillips","minuti":100},
#                  {"idFilm":8,"titolo":"Joker","anno":2019,"regista":"Todd Phillips","minuti":122},
#                  {"idFilm":9,"titolo":"Avatar","anno":2010,"regista":"James Cameron","minuti":162},
#                  {"idFilm":10,"titolo":"Titanic","anno":1997,"regista":"James Cameron","minuti":195},
#                  {"idFilm":11,"titolo":"Avenegers: Infinity War","anno":2018,"regista":"Anthony e Joe Russo","minuti":149},
#                  {"idFilm":12,"titolo":"Avenegers: Endgame","anno":2019,"regista":"Anthony e Joe Russo","minuti":181},
#                  {"idFilm":13,"titolo":"Captain America: Civil War","anno":2016,"regista":"Anthony e Joe Russo","minuti":147},
#                  {"idFilm":14,"titolo":"Shutter Island","anno":2010,"regista":"Martin Scorsese","minuti":138}])
#ins=generi.insert()
#conn.execute(ins,[{"genere":"Drammatico","film":1},
#                  {"genere":"Thriller","film":1},
#                  {"genere":"Giallo","film":1},
#                  {"genere":"Thriller","film":2},
#                  {"genere":"Drammatico","film":2},
#                  {"genere":"Azione","film":3},
#                  {"genere":"Fantascienza","film":3},
#                  {"genere":"Thriller","film":3},
#                  {"genere":"Avventura","film":3},
#                  {"genere":"Thriller","film":4},
#                  {"genere":"Drammatico","film":4},
#                  {"genere":"Fantascienza","film":4},
#                  {"genere":"Commedia","film":5},
#                  {"genere":"Commedia","film":6},
#                  {"genere":"Commedia","film":7},
#                  {"genere":"Drammatico","film":8},
#                  {"genere":"Thriller","film":8},
#                  {"genere":"Noir","film":8},
#                  {"genere":"Fantascienza","film":9},
#                  {"genere":"Azione","film":9},
#                  {"genere":"Avventura","film":9},
#                  {"genere":"Drammatico","film":10},
#                  {"genere":"Sentimentale","film":10},
#                  {"genere":"Storico","film":10},
#                  {"genere":"Azione","film":10},
#                  {"genere":"Catastrofico","film":10},
#                  {"genere":"Fantascienza","film":11},
#                  {"genere":"Azione","film":11},
#                  {"genere":"Avventura","film":11},
#                  {"genere":"Fantascienza","film":12},
#                  {"genere":"Azione","film":12},
#                  {"genere":"Avventura","film":12},
#                  {"genere":"Azione","film":13},
#                  {"genere":"Avventura","film":13},
#                  {"genere":"Thriller","film":14},
#                  {"genere":"Noir","film":14}])
#ins=sale.insert()
#conn.execute(ins,[{"idSala":1,"numPosti":50,"disponibile":True},
#                  {"idSala":2,"numPosti":25,"disponibile":True},
#                  {"idSala":3,"numPosti":25,"disponibile":False},
#                  {"idSala":4,"numPosti":75,"disponibile":True},
#                  {"idSala":5,"numPosti":100,"disponibile":True}])
#ins=proiezioni.insert()
#conn.execute(ins,[#{"orario":datetime(2017,10,4,21,30),"prezzo":9.5,"film":1,"sala":1},
                  #{"orario":datetime(2018,6,17,16,45),"prezzo":10.0,"film":1,"sala":2},
                  #{"orario":datetime(2017,12,7,00,00),"prezzo":8.5,"film":1,"sala":1},
                  #{"orario":datetime(2018,3,24,22,30),"prezzo":9.5,"film":1,"sala":3},
                  #{"orario":datetime(2019,8,14,19,30),"prezzo":9.,"film":2,"sala":3},
                  #{"orario":datetime(2020,10,4,21,30),"prezzo":9.5,"film":2,"sala":4},
                  #{"orario":datetime(2020,7,15,20,15),"prezzo":9.5,"film":2,"sala":4},
                  #{"orario":datetime(2017,10,4,21,30),"prezzo":9.5,"film":2,"sala":5},
                  #{"orario":datetime(2019,4,15,21,30),"prezzo":10.5,"film":2,"sala":1},
                  #{"orario":datetime(2020,6,27,15,30),"prezzo":7.5,"film":3,"sala":2},
                  #{"orario":datetime(2020,11,4,21,30),"prezzo":9.5,"film":3,"sala":5},
                  #{"orario":datetime(2017,1,1,21,30),"prezzo":9.0,"film":3,"sala":5},
                  #{"orario":datetime(2019,5,5,21,30),"prezzo":9.5,"film":4,"sala":4},
                  #{"orario":datetime(2018,5,4,21,30),"prezzo":9.5,"film":4,"sala":3},
                  #{"orario":datetime(2016,5,4,21,30),"prezzo":9.5,"film":4,"sala":2},
                  #{"orario":datetime(2020,4,4,21,30),"prezzo":9.5,"film":4,"sala":1},
                  #{"orario":datetime(2020,7,4,21,30),"prezzo":9.5,"film":5,"sala":1},
                  #{"orario":datetime(2020,7,1,21,30),"prezzo":9.0,"film":5,"sala":2},
                  #{"orario":datetime(2014,10,4,21,30),"prezzo":9.5,"film":5,"sala":3},
                  #{"orario":datetime(2013,10,4,21,30),"prezzo":9.5,"film":5,"sala":3},
                  #{"orario":datetime(2013,11,4,21,30),"prezzo":9.5,"film":5,"sala":4},
                 #### #{"orario":datetime(2017,10,4,21,30),"prezzo":9.5,"film":6,"sala":1},
                  #{"orario":datetime(2017,10,4,21,30),"prezzo":9.5,"film":6,"sala":1},
                  #{"orario":datetime(2017,10,4,21,30),"prezzo":9.5,"film":6,"sala":1},
                  #{"orario":datetime(2017,10,4,21,30),"prezzo":9.5,"film":7,"sala":1},
                  #{"orario":datetime(2017,10,4,21,30),"prezzo":9.5,"film":7,"sala":1},
                  #{"orario":datetime(2017,10,4,21,30),"prezzo":9.5,"film":7,"sala":1},
                  #{"orario":datetime(2017,10,4,21,30),"prezzo":9.5,"film":7,"sala":1},
                  #{"orario":datetime(2017,10,4,21,30),"prezzo":9.5,"film":1,"sala":1},
                  ####{"orario":datetime(2019,4,15,20,30),"prezzo":10.5,"film":2,"sala":1},
                  #{"orario":datetime(2019,5,10,23,30),"prezzo":9.5,"film":6,"sala":2}])


#conn.close()


def user_email_query(usr_email):
    conn = engine.connect()
    s=select([utenti]).where(utenti.c.email==bindparam("email"))
    rs = conn.execute(s,email=usr_email)
    user = rs.fetchall()
    conn.close()
    if(len(user)==0):
        raise EmptyResultException
    return user[0]

def aggiungi_utente_query(email,pwd,nomeUtente,annoNascita,sesso,provincia):
    if("maschio" in sesso):
        sesso="M"
    elif("femmina" in sesso):
        sesso="F"
    conn=engine.connect()
    trans=conn.begin()
    try:
        s=select([utenti]).where(utenti.c.email==bindparam("eml"))
        res=conn.execute(s,eml=email)
        res=res.fetchall()
        if(len(res)!=0):
            print(len(res))
            raise ResultException
        ins=utenti.insert()
        conn.execute(ins,[{"email":email,"nomeUtente":nomeUtente,"pwd":pwd,"annoNascita":annoNascita,"sesso":sesso,"provincia":provincia,"gestore":False}])
        trans.commit()
        conn.close()
    except:
        trans.rollback()
        conn.close()
        raise ResultException

def posti_cliente_query(email):
    conn=engine.connect()
    s=select([biglietti.c.posto,proiezioni.c.orario,film.c.titolo,proiezioni.c.sala]).where(and_(biglietti.c.cliente==bindparam("email"),
                proiezioni.c.idProiezione==biglietti.c.proiezione,film.c.idFilm==proiezioni.c.film,proiezioni.c.orario>datetime.now()))
    res=conn.execute(s,email=email)
    res=res.fetchall()
    return res

def titolo_film_query(idFilm):
    conn=engine.connect()
    s=select([film.c.titolo]).where(film.c.idFilm==bindparam("film"))
    res=conn.execute(s,film=idFilm)
    res=res.fetchall()
    if(len(res)==0):
        conn.close()
        raise EmptyResultException
    conn.close()
    return res[0]["titolo"]

def orarioFilm_proiezione_query(id_proiezione):
    conn=engine.connect()
    s=select([proiezioni.c.orario,film.c.titolo,proiezioni.c.sala]).where(and_(proiezioni.c.idProiezione==bindparam("proiez"),proiezioni.c.film==film.c.idFilm))
    res=conn.execute(s,proiez=id_proiezione)
    res=res.fetchall()
    if(len(res)==0):
        conn.close()
        raise EmptyResultException
    conn.close()
    return res[0]

def proiezioni_film_query(id_film): #Ritorna le proiezioni future del film con id id_film
    conn=engine.connect()
    s=select([proiezioni]).where(and_(proiezioni.c.film==film.c.idFilm,film.c.idFilm==bindparam('id'),proiezioni.c.orario>datetime.now(),
                sale.c.idSala==proiezioni.c.sala,sale.c.disponibile))
    res=conn.execute(s,id=id_film)
    res=res.fetchall()####
    conn.close()
    if(len(res)==0):
        raise EmptyResultException
    return res

def film_titolo_query(titoloFilm): #data una stringa titoloFilm ritorna i film che hanno come titolo una stringa che contiene al suo interno titoloFilm (titoloFilm e' sottostringa)
    conn=engine.connect()
    s=select([film]).where(film.c.titolo.contains(bindparam('titolo')))
    res=conn.execute(s,titolo=titoloFilm)
    res=res.fetchall()####
    conn.close()
    if(len(res)==0):
        raise  EmptyResultException
    return res

def deleteDup(x): #data una lista ritorna una lista senza duplicati
  return list(dict.fromkeys(x))

def generi_query(): #ritorna tutti i generi memorizzati nel database
    conn=engine.connect()
    res=conn.execute(select([generi.c.genere]))
    list=[x["genere"] for x in res.fetchall()]
    conn.close()
    return deleteDup(list)

def film_genere_query(genereFilm): #ritorna i film che hanno come genere il genere ricevuto in input (genereFilm)
    conn=engine.connect()
    s=select([film]).where(and_(generi.c.film==film.c.idFilm,generi.c.genere==bindparam('genere')))
    res=conn.execute(s,genere=genereFilm)
    print(res)
    res=res.fetchall()####
    print(res)
    conn.close()
    if(len(res)==0):
        raise  EmptyResultException
    return res

def postiLiberi_proiezione_query(id_proiezione):
    conn=engine.connect()
    s=select([sale.c.disponibile]).where(and_(proiezioni.c.idProiezione==bindparam('id'),sale.c.idSala==proiezioni.c.sala))
    res=conn.execute(s,id=id_proiezione)
    res=res.fetchall()
    if(len(res)==0 or (not res[0]["disponibile"])):
        conn.close()
        raise ResultException
    s=select([proiezioni.c.orario]).where(proiezioni.c.idProiezione==bindparam('id'))
    res=conn.execute(s,id=id_proiezione)
    res=res.fetchall()
    if(len(res)==0 or res[0]["orario"]<datetime.now()):
        conn.close()
        raise ResultException


    s=select([sale.c.numPosti]).where(and_(proiezioni.c.idProiezione==bindparam('id'),sale.c.idSala==proiezioni.c.sala))
    res=conn.execute(s,id=id_proiezione)
    postiTotali=res.fetchone()["numPosti"]
    s=select([biglietti.c.posto]).where(biglietti.c.proiezione==bindparam('id'))
    res=conn.execute(s,id=id_proiezione)
    list=res.fetchall()
    list= [x["posto"] for x in list]
    list= [x for x in range(0,postiTotali) if x not in list]
    conn.close()
    if(len(list)==0):
        raise EmptyResultException
    return list

def compra_biglietto_query(posto,id_proiezione,email):  ###########TRANSAZIONI ED ECCEZIONI SPECIFICHE
    conn=engine.connect()
    #s=select([biglietti.c.posto]).where(biglietti.c.proiezione==bindparam('id')) ####USO DELLA FUNZIONE POSTI LIBERI
    #res=conn.execute(s,id=id_proiezione)
    #list=res.fetchall()
    #list= [x["posto"] for x in list]
    #if(posto in list):
    #    raise RuntimeError("Query Error")
    trans=conn.begin()

    try:
        if(posto in postiLiberi_proiezione_query(id_proiezione)):
            raise ResultException
        ins=biglietti.insert()
        conn.execute(ins,[{"posto":posto,"proiezione":id_proiezione,"cliente":email}])
        trans.commit()
        conn.close()
    except:
        trans.rollback()
        conn.close()
        raise ResultException