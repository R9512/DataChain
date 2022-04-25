
from re import L
from warnings import filters
from flask import request
from flask import Flask
from flask_cors import CORS
from flask import jsonify
from matplotlib.font_manager import json_dump
from mysqlx import Schema
import requests
import mysql.connector
import json
import river as r
import pickle as pkl
import csv
import ast
import io
from sklearn.model_selection import learning_curve
app = Flask(__name__)
app.secret_key = '_5#y2L"F4Q8z\n\xec]/'
cors = CORS(app)
ALLOWED_EXTENSIONS = {'pkl'}#Need to add H5 for the future
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Rodda95*"
)
my_cursor = mydb.cursor()
my_cursor.execute('USE swami')

#======IncrementalLearning======
def IncreLinerReg(hp):
    lr = float(hp[0])
    model = (r.preprocessing.StandardScaler() |r.linear_model.LinearRegression(intercept_lr=lr))
    return(model)
def IncreLogReg(hp):
    lr = float(hp[0])#optimizer 
    model = (r.preprocessing.StandardScaler() |r.linear_model.LogisticRegression(optimizer=r.optim.SGD(lr)))
    return(model)
def IncreSofReg(_):
    model = (r.preprocessing.StandardScaler() |r.linear_model.SoftmaxRegression())
    return(model)
def IncreALMA(hp):
    model = (r.preprocessing.StandardScaler() |r.linear_model.ALMAClassifier())
    return(model)
def IncreAdaClass(hp):
    a,b = int(hp[0]),int(hp[1])
    model = r.ensemble.AdaBoostClassifier(
    model=(r.tree.HoeffdingTreeClassifier(split_criterion='gini',split_confidence=1e-5,grace_period=2000 )),n_models=a,seed=b)
    return(model)

def IncreRanFClass(hp):
    a,b = int(hp[0]),int(hp[1])
    model = r.ensemble.AdaptiveRandomForestClassifier( n_models=a,seed=b )
    return(model)
def IncreRanFReg(hp):
    a,b = int(hp[0]),int(hp[1])
    model = (r.preprocessing.StandardScaler() |r.ensemble.AdaptiveRandomForestRegressor(n_models=a, seed=b) )
    return(model)
def IncreBagReg(hp):
    a,b,c= int(hp[0]),int(hp[1]),float(hp[2])

    model = (r.preprocessing.StandardScaler() |r.ensemble.BaggingRegressor( model=r.linear_model.LinearRegression(intercept_lr=c),n_models=a,seed=b ))
    return(model)
def IncreEFDT(hp):
    a,b= int(hp[0]),int(hp[1])
    model = r.tree.ExtremelyFastDecisionTreeClassifier(grace_period=a,split_confidence=1e-5,min_samples_reevaluate=b)
    return(model)
def IncreHATC(hp):
    a,b,c = int(hp[0]),int(hp[1]),int(hp[2])
    model = r.tree.HoeffdingAdaptiveTreeClassifier(grace_period=a,split_confidence=1e-5,leaf_prediction='nb', nb_threshold=b,seed=c )
    return(model)
def IncreHATR(hp):
    a,b,c = int(hp[0]),float(hp[1]),int(hp[2])
    model = (r.preprocessing.StandardScaler() |r.tree.HoeffdingAdaptiveTreeRegressor(grace_period=a,leaf_prediction='adaptive',model_selector_decay=b,seed=c) )
    return(model)
def IncreSGTR(hp):
    a,b,c,d = float(hp[0]),float(hp[1]),int(hp[2]),float(hp[3])
    model = r.tree.SGTRegressor(     delta=a,     lambda_value=b,     grace_period=c,     feature_quantizer=r.tree.splitter.DynamicQuantizer(std_prop=d) )
    return (model)
def IncreDBS(hp):
    a,b,c,d,e = float(hp[0]),float(hp[1]),float(hp[2]),float(hp[3]),float(hp[4])
    model = r.cluster.DBSTREAM(clustering_threshold = a,fading_factor = b,cleanup_interval = c,intersection_factor = d,minimum_weight = e)
    return(model)
def IncreDen(hp):
    a,b,c,d,e = float(hp[0]),float(hp[1]),float(hp[2]),float(hp[3]),int(hp[4])
    model = r.cluster.DenStream(decaying_factor =a,beta = b,mu = c,epsilon = d,n_samples_init=e)
    return(model)
def IncreKM(hp):
    a,b,c,d = int(hp[0]),float(hp[1]),float(hp[2]),int(hp[3])
    model = r.cluster.KMeans(n_clusters=a, halflife=b, sigma=c, seed=d)
    return(model)

def IncreSKM(hp):
    a,b,c,d = int(hp[0]),float(hp[1]),float(hp[2]),int(hp[3])
    model = r.cluster.STREAMKMeans(n_clusters=a, halflife=b, sigma=c, seed=d)
    return(model)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        usern = str(request.json['name'])
        sign = str(request.json['sign'])
        my_cursor.execute("select * from users where username='"+usern+"' and signature='"+sign+"'")
        count = 0
        for _ in my_cursor:
            count+=1
        print(count)
        if(count == 0):
            return(jsonify({'output':'wronguser'}))
        return(jsonify({'output':'rightuser'}))
@app.route('/jsairam',methods=["GET"])
def cryptorates():
    temp = requests.get("http://min-api.cryptocompare.com/data/blockchain/mining/calculator?fsyms=ETH&tsyms=USD&api_key=9535778365ca5abef2e923dd3e18f2872299c60b88240d0b02842e574913dd6d").content
    my_json = temp.decode('utf8').replace("'", '"')
    data = json.loads(my_json)
    s = json.dumps(data, indent=4, sort_keys=True)  
    s = json.loads(s)  
    s = s['Data']['ETH']
    final = {}
    final['price'] = s["Price"]["USD"]
    s = s["CoinInfo"]
    final["bn"],final['br'],final['bt'],final['hr'],final['tc']= s['BlockNumber'],s['BlockReward'],s['BlockTime'],s['NetHashesPerSecond'],s['TotalCoinsMined']
    #Need To add fake things when net is not availabe=>pr,bn,br,bt,ht,tc,
    return(jsonify(final))


@app.route('/newaccount', methods=['GET', 'POST'])
def newaccount():
    print("swami Let It asdighasasdgad")
    if(request.method=='POST'):
        print("In The New Accoutn the recieved data is")     
        uname = request.json['name']
        sing  = request.json['sign']
        addr  = request.json['addr']
        my_cursor.execute("insert into users (username,address,signature,balance) values ('"+uname+"','"+addr+"','"+sing+"',0);")
        mydb.commit()
        print(my_cursor.rowcount, "record inserted.")    
        return(jsonify({'output':'created'}))


@app.route('/predict',methods=['GET'])
def modeldetails():
    st = "select modid,title,tags from models2;"
    my_cursor.execute(st)
    all = my_cursor.fetchall()
    tosend=[]
    temp={}
    for x in all:
        temp['modelid'] = x[0]
        temp['title'] = x[1]
        temp['tags'] = x[2]
        print(temp,type(temp))
        tosend.append(json.dumps(temp))
    #print(tosend)
    return({"output":tosend})

@app.route('/model',methods = ['GET','POST'])
def actualpredictor():
    if(request.method =="GET"):
        id = request.args.get("id")
        st = "select * from models2 where modid="+id+";"
        my_cursor.execute(st)
        all = my_cursor.fetchone()
        temp = {}
        temp['title'] = all[1]
        temp['desc'] = all[2]
        temp['schema'] = all[3]
        temp['tags'] = all[6]
        print(temp['schema'])
        temp = json.dumps(temp)
        return({'output':temp})
    if(request.method =="POST"):
        temp = request.json["input"]
        modid = request.json["modid"]
        print(temp)
        st = "select * from models2 where modid="+modid+";"
        my_cursor.execute(st)
        all = my_cursor.fetchone()
        
        model = pkl.loads(all[5])
        
        temp=model.predict_one(temp)
        return(jsonify({'output':temp}))


@app.route('/contribute',methods = ['GET','POST'])
def actualcontributor():

    if(request.method =="GET"):
        id = request.args.get("id")
        print(id)
        st = "select method,learning,title,ldesc,tags from model6 where modelid="+id+";"
        my_cursor.execute(st)
        all = my_cursor.fetchone()
        st = "select mschema from model7 where modelid="+id+";"
        my_cursor.execute(st)
        all1 = my_cursor.fetchone()
        tosend = [all,all1]
        return(jsonify(tosend))
    if(request.method =="POST"):
        temp1 = ""
        temp = request.json["data"]
        useradd = str(request.json["user"])
        
        modid = request.json["modid"]
        learning = request.json["learning"]
        
        st = "select filter,actual,predict from model7 where modelid="+modid+";"
        my_cursor.execute(st)
        all = my_cursor.fetchall()
        print(all[0])
        filter = pkl.loads(all[0][0])

        if(learning=="Incremental Learning"):
            print("Inside Incremental Learning")
            st = "select mschema from model7 where modelid="+modid+";"
            my_cursor.execute(st)
            schema = my_cursor.fetchone()
            schema = schema[0]

            schema = ast.literal_eval(schema)
            print("*"*95,schema,type(schema))
            schema = list(schema.values())
            for ind,x in enumerate(temp.keys()):
                if(schema[ind] == "float"):
                    temp[x] = float(temp[x])
                if(schema[ind]=="int"):
                    temp[x] = int(temp[x])
                if(schema[ind]=="bool"):
                    temp[x] = bool(temp[x])
            yvar = temp[all[0][2]]
            temp.pop(all[0][2])
            print(temp,"",yvar)
            
            temp1 = filter.predict_one(temp)
            filter  = pkl.dumps(filter)
            print("#"*95)
            print("The Prediction is ",temp1)
            print(temp,yvar,str(temp),str(yvar),str(temp)==str(yvar),temp1==yvar)
            print(type(temp1),type(yvar))
            if(temp1==yvar):
                
                model = pkl.loads(all[0][1])
                model.learn_one(temp,yvar)
                model = pkl.dumps(model)
                st = "update model6 set reached=reached+1 where modelid="+modid+";"
                my_cursor.execute(st)
                
                st = "update model7 set filter=%s , actual=%s where modelid="+modid+";"

                my_cursor.execute(st,(filter,model))
                
                st = "select bounty from model6 where modelid ="+modid+";"
                my_cursor.execute(st)
                temp = my_cursor.fetchone()[0]
                print(temp)
                st = "update users set bounty=bount+"+str(temp)+" where address="+useradd+";"
                mydb.commit()
                return(jsonify({'output':"1"}))
        else:
            print("rejected")
            return(jsonify({'output':"0"}))


@app.route('/newmodel',methods=["POST"])
def modelcreator():
        modelname = str(request.json["model"])
        learning = str(request.json["learning"])
        schema = str(request.json["schema"])
        hp = (request.json["hp"])
        title = str(request.json["title"])
        tags = str(request.json["tags"])
        target = str(request.json["target"])
        sd = str(request.json["sd"])
        ld = str(request.json["fd"])
        dssell = str(request.json["dssell"])
        modsell =str(request.json["modsell"])
        owner = str(request.json["owner"])
        bounty = float(request.json["bounty"])
        print("Bounty",bounty)
        target = int(request.json["target"])
        predict =str(request.json["predict"])
        if(learning=="Incremental Learning" or learning=="Machine Learning"):
            if(modelname=="Linear Regression"):                
                model = IncreLinerReg(hp)
            if(modelname=="Logistic Regression"):
                model = IncreLogReg(hp)
            if(modelname=="Softmax Regression"):
                model = IncreSofReg(hp)            
            if(modelname=="ALMA Classifier"):#Need To Work ON it int eh Fromtend as there is no data enough for it
                model = IncreALMA(hp)
            if(modelname=="Adaboost Classifier"):
                model = IncreAdaClass(hp)
            if(modelname=="AdaptiveRandom Forest Classifier"):
                model = IncreRanFClass(hp)
            if(modelname=="AdaptiveRandom Forest Regressor"):
                model = IncreRanFReg(hp)
            if(modelname=="Bagging Regressor"):
                model = IncreBagReg(hp)
            if(modelname=="Extremely Fast Decision Tree"):
                model = IncreEFDT(hp)
            if(modelname=="Hoeffding Adaptive Tree Classifier"):
                model = IncreHATC(hp)            
            if(modelname=="Hoeffding Adaptive Tree Regressor"):
                model = IncreHATR(hp)            
            if(modelname=="SGT Regressor"):#Need To Work ON it int eh Fromtend as there is no data enough for it
                model = IncreSGTR(hp)            
            if(modelname=="DBSTREAM"):
                model = IncreDBS(hp)
            if(modelname=="DenStream"):
                model = IncreDen(hp)
            if(modelname=="DenStream"):
                model = IncreDen(hp)
            if(modelname=="KMeans"):
                model = IncreKM(hp)
            if(modelname=="STREAMKMeans"):
                model = IncreSKM(hp)
        
        st = f"insert into model6 (owner,method,learning,rating,bounty,target,reached,title,sdesc,ldesc,tags,private,datasetsell,modelsell) values('{owner}','{modelname}','{learning}',0,{bounty},{target},0,'{title}','{sd}','{ld}','{tags}',false,{dssell},{modsell});"
        my_cursor.execute(st)
        mydb.commit()
        modeltemp = pkl.dumps(model)
        st = "SELECT modelid,owner FROM model6 ORDER BY modelid DESC LIMIT 1;"
        my_cursor.execute(st)
        temp = my_cursor.fetchone()
        temp,owner= temp[0],temp[1]
        st = f'insert into model7 (modelid,owner,mschema,predict,filter,actual) values({temp},"{owner}","{schema}","{predict}",%s,%s);'
        my_cursor.execute(st,(modeltemp,modeltemp))
        mydb.commit()
        return(jsonify({"modid":temp,"userid":owner,"proceed":"1","title":title}))

@app.route('/mymodels',methods=["POST"])
def mymodelspage():
    temp = ""
    temp = str(request.json['account'])
    
    st = "select modelid,title,sdesc,tags from model6 where owner = '"+temp+"' and reached=0;"
    my_cursor.execute(st)
    all = my_cursor.fetchall()
    print(all)
    tosend = []
    toconfig = []
    temp = {}
    for x in all:
        temp['id'],temp['title'],temp['sdesc'],temp['tags'] = x[0],x[1],x[2],x[3]
        toconfig.append(json.dumps(temp))
    
    temp = str(request.json['account'])
    st = "select modelid,title,sdesc,tags from model6 where owner = '"+temp+"' and reached>0;"
    my_cursor.execute(st)
    all = my_cursor.fetchall()
    totune = []
    temp = {}
    for x in all:
        temp['id'],temp['title'],temp['sdesc'],temp['tags'] = x[0],x[1],x[2],x[3]
        totune.append(json.dumps(temp))
    tosend.append(toconfig)
    tosend.append(totune)

    return(jsonify({"output":tosend}))

@app.route('/configure',methods=["GET","POST"])
def configurer():
    if(request.method=="GET"):
        print("Herer")
        st = "select title,method,learning,sdesc,ldesc,tags from model6 where modelid='"+str(request.args.get("id"))+"';"
        my_cursor.execute(st)
        print(st)
        result = my_cursor.fetchone()
        tosend ={}
        tosend["title"],tosend["method"],tosend["learning"],tosend["sdesc"],tosend["ldesc"],tosend["tags"] = result
        return(jsonify({"output":tosend}))
    if (request.method=='POST'):
        print("Swami")
        my_files = request.files.get("model") 
        data = my_files.stream.read()
        title = str(request.form.get('title'))
        learning = str(request.form.get("lear"))
        stream = io.StringIO(data.decode("UTF8"), newline=None) 
        reader = csv.DictReader(stream)

        st = "select mschema,filter from model7 where modelid='"+title+"';"

        my_cursor.execute(st)
        gotten = my_cursor.fetchall()
        schema = ast.literal_eval(gotten[0][0])
        model = pkl.loads(gotten[0][1])
        if(learning=="Incremental Learning"):
            count = 0
            schema = list(schema.values())#This is for the Incremental Learning only need to check for it also
            for record in reader:
                for ind,x in enumerate(record.keys()):
                    if(schema[ind] == "float"):
                        record[x] = float(record[x])
                    if(schema[ind]=="int"):
                        record[x] = int(record[x])
                    if(schema[ind]=="bool"):
                        record[x] = bool(record[x])
                tork = list(record.keys())[-1]
                yvar = record[tork]
                record.pop(tork)
                model.learn_one(record,yvar)
                count+= 1
            st = "update model6 set reached="+str(count)+" where modelid="+title+";"
            my_cursor.execute(st)
            st = "update model7 set filter=%s , actual=%s where modelid="+title+";"
            modeltemp = pkl.dumps(model)
            my_cursor.execute(st,(modeltemp,modeltemp))
            mydb.commit()


        print("Trained adn It is done*******************************")
        return("Swami")
@app.route('/modelstore',methods=["GET","POST"])
def modelstoredatareturner():
    if(request.method=="GET"):
        print("Swami")
        st = "select modelid,title,tags,reached,target,bounty,sdesc from model6;"
        my_cursor.execute(st)
        all = my_cursor.fetchall()
            
        return(jsonify(all))
        




