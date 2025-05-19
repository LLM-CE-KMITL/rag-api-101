# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

from rag_helpers import RAG_OpenSearch, EmbeddingModel
import requests

##############################################
#############      Pre-Process    ############
##############################################


############# SET EMBEDDING MODEL ############


em = EmbeddingModel(EmbeddingModel.BGE_M3)


############# INITIAL OPENSEARCH ############


HOST = 'localhost'
PORT = 9200
USERNAME = 'admin'
PASSWORD = '@PassWord.1234'

ros = RAG_OpenSearch()
ros.connect_vector_db(host=HOST, port=PORT, username=USERNAME, password=PASSWORD)
ros.set_embedding_model(em)



############# CREATE VECTOR SPACE ############


VEC_SPACE = 'rag_1'

ros.delete_vector_space(VEC_SPACE)
ros.create_vector_space(VEC_SPACE)


############# ADD MANY ITEMS and QUERY ############


items = [
  { "doc": "food", "text": "ผัดไทยเป็นอาหารไทยที่มีชื่อเสียงไปทั่วโลก ใช้วุ้นเส้นหรือเส้นจันท์ผัดกับไข่ เต้าหู้ กุ้งแห้ง ถั่วลิสงบด และถั่วงอก ปรุงรสด้วยน้ำมะขามเปียก น้ำปลา น้ำตาลปี๊บ และพริกป่น ให้รสเปรี้ยว หวาน เค็ม เผ็ดกลมกล่อม" },

  { "doc": "food", "text": "ต้มยำกุ้งเป็นเมนูซุปเผ็ดร้อนที่ขึ้นชื่อของไทย ใช้กุ้งสด เห็ด ข่า ตะไคร้ ใบมะกรูด และพริกสด ปรุงรสด้วยน้ำมะนาว น้ำปลา และพริกเผา รสชาติจัดจ้าน หอมสมุนไพรไทย" },

  { "doc": "food", "text": "แกงเขียวหวานเป็นอาหารไทยที่มีรสชาติเข้มข้น ใช้พริกแกงเขียวหวานปรุงกับกะทิ ใส่เนื้อไก่ ลูกชิ้นปลา หรือหมู พร้อมมะเขือเปราะ ใบโหระพา และพริกชี้ฟ้าแดง เสิร์ฟกับข้าวสวยร้อน ๆ" },

  { "doc": "food", "text": "ส้มตำเป็นอาหารอีสานยอดนิยม ทำจากมะละกอดิบขูดฝอย คลุกเคล้ากับน้ำปลา มะนาว พริก กระเทียม มะเขือเทศ และถั่วฝักยาว ให้รสจัดจ้าน เปรี้ยว เผ็ด เค็มและหวานเล็กน้อย" },

  { "doc": "food", "text": "ข้าวซอยเป็นอาหารเหนือที่มีเอกลักษณ์ ใช้เส้นบะหมี่ไข่ในน้ำแกงกะทิเข้มข้น ใส่เนื้อไก่หรือเนื้อวัว โรยหน้าด้วยบะหมี่ทอดกรอบ เสิร์ฟพร้อมหอมแดงดอง มะนาว และผักดอง" },

  { "doc": "food", "text": "มัสมั่นไก่เป็นแกงไทยที่ได้รับอิทธิพลจากอาหารอินเดีย ใช้พริกแกงมัสมั่น ผัดกับกะทิ ใส่เนื้อไก่ มันฝรั่ง และถั่วลิสง รสชาติหวาน มัน เค็ม และหอมเครื่องเทศ" },

  { "doc": "food", "text": "ข้าวผัดกะเพราเป็นเมนูจานด่วนที่คนไทยนิยม ใช้เนื้อหมูหรือไก่ผัดกับกระเทียม พริก และใบกะเพรา ปรุงรสด้วยซีอิ๊วขาว น้ำปลา และน้ำตาล เสิร์ฟกับข้าวสวยและไข่ดาว" },

  { "doc": "food", "text": "แกงส้มชะอมไข่เป็นอาหารใต้ที่นิยมรับประทาน ใช้พริกแกงส้มปรุงกับน้ำและกุ้ง ใส่ชะอมไข่หั่นเป็นชิ้นเล็ก ๆ รสเปรี้ยว เผ็ด กลมกล่อมจากน้ำมะขามเปียก" },

  { "doc": "food", "text": "ลาบหมูเป็นอาหารอีสานที่มีรสจัดจ้าน ทำจากหมูสับคลุกกับน้ำมะนาว น้ำปลา ข้าวคั่ว และพริกป่น ใส่หอมแดงซอย และต้นหอมซอย กินคู่กับผักสด" },

  { "doc": "food", "text": "ขนมจีนน้ำยาเป็นเมนูเส้นที่คนไทยนิยม ประกอบด้วยขนมจีนราดด้วยน้ำยาปลาที่ปรุงจากเครื่องแกง หัวกะทิ และเนื้อปลา ปรุงรสจัดจ้าน กินคู่กับผักสด เช่น ถั่วฝักยาว ถั่วงอก และแตงกวา" }
]



ros.store_many_items(VEC_SPACE, items)


# ros.query(VEC_SPACE, "อาหารเหนือมีอะไร", 2)

"""
data = {
   "model":"llm",
   "messages":[
      {
         "role":"system",
         "content":"You are a useful assistant."
      },
      {
         "role":"user",
         "content":"อาหารเหนือมีอะไรบ้าง"
      }
   ]
}
    
request = data




"""

##############################################
########     HELPERS  FUNCTIONS       ########
##############################################

def get_prompt(query, context):
    template = '''
      You are an AI thai language model assistant.
      Answer the question based ONLY on the following context.
    
      {context}
    
      Original question: {question}"""
    '''.replace('\n',' ')
    return template.format(question=query, context=context)


def to_chat(data):
    url = 'http://localhost:1234/v1/chat/completions'
    headers = {'Content-Type': 'application/json; charset=utf-8'}
        
    last_query = data['messages'][-1]['content']
        
    context_res = ros.query(VEC_SPACE, last_query, 2)
    print("QUERY: ", last_query)
    print("CONTEXT: last_query", context_res)

    context_txt = "; ".join([x[0] for x in context_res])
    
    prompt = get_prompt(last_query, context_txt)
    
    data['messages'][-1]['content'] = prompt
    
    response = requests.post(url, headers=headers, json=data)

    return response.json()



#############################################
#############################################
######             API                #######
#############################################
#############################################


app = Flask(__name__)
cors = CORS(app) # allow CORS for all domains on all routes.
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/v1/chat/completions', methods=["POST"])
@cross_origin()
def chat_completions():
    res = to_chat(request.json)
    res = jsonify(res)
    return res




if __name__ == '__main__':
    app.run()
    
    
##########





