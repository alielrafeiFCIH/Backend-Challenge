from flask import Flask, render_template,request,redirect, jsonify
from flask_cors import CORS
import data.mongosetup as mongosetup
import service.data_service as svc
from form import machineform,podform
import json
app = Flask(__name__)#reference the file 
app.config['SECRET_KEY'] = "codebt3na"
mongosetup.global_init()
@app.route('/')
def index():
    return "Challenge"

@app.route('/FilterMachine',methods=['GET','POST'])
def filter_machine():
    form = machineform()
    if(request.method=='POST'):
         if form.is_submitted():
            product_type=request.form['product_type']
            water_line=request.form['water_line']
            print(product_type)
            obj = svc.machine_filter(product_type,water_line)
            return jsonify(obj)
    return render_template('query_machine.html',form=form)

@app.route('/FilterPods',methods=['GET','POST'])
def filter_pods():
    form = podform()
    if(request.method=='POST'):
         if form.is_submitted():
            product_type=request.form['product_type']
            pack_size=request.form['pack_size']
            flavor=request.form['flavor']
            obj = svc.pods_filter(product_type,flavor,pack_size)
            return jsonify(obj)
    return render_template('query_pod.html',form=form)
if __name__ == "__main__":
    app.run(debug=True)