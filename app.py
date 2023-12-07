import json
from flask import Flask, render_template, request
import newMain
app = Flask(__name__,static_folder='templates\static')
from seoanalyzer import __main__
# @app.route("/")
# def hello():
#   return "Hello World!"
@app.route("/")
def first_Page():
  return render_template('index.html')

# def redirectt():
#   url=request.form['url']
#   print(url)
#   l=[]
#   output=newMain.main(url)
#   # for i in output:
#   #     print(i)
#   #     # l.append[i]
#   #     for x in output[i]:
#   #         print(x,':',output[i][x])
#   # resultList = [(key, value) for key, value in output.items()]
#   # print(type(resultList))
#   # render_template('results.html',res=json.dumps(resultList, indent=4, separators=(',', ': ')))
  
#   #print(output)
#   return render_template('results.html',res=output )
@app.route("/seoanalyzer",methods=['POST'])
def redirectt():
  url=request.form['url']
  formatt=request.form['optype']
  print("in app.py" ,formatt)
  print(url)
  res=newMain.main(url,formatt)
  print("result 1 type",type(res))
  print('huhhhh')
  print(res)
  # if formatt=='html':
  #   return render_template('extra.html',form=res)
  #res=res.replace('\n','<br>')

  return render_template('results.html',res=res)

  

if __name__ == "__main__":
  app.debug = True
  app.run()