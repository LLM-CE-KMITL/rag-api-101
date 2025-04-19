# RAG API

## Overall
![RAG 101 System Architecture](rag-101-flow.jpg)


## LM Studio API
* Instruction: https://github.com/LLM-CE-KMITL/python-call-lmstudio

## OpenSearch (Vector DB)
* Instruction: https://github.com/LLM-CE-KMITL/opensearch-101

## Run Flask API
```
python rag_api.py
```

## Try Chatting
* Open my-chat.html

## Example Input and Output

### Chat UI --> RAG API
* Request
```
{
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
```

* Response
```
{
   "choices":[
      {
         "finish_reason":"stop",
         "index":0,
         "logprobs":null,
         "message":{
            "content":"ข้าวซอยเป็นอาหารเหนือที่มีเอกลักษณ์",
            "role":"assistant"
         }
      }
   ],
   "created":1745069089,
   "id":"chatcmpl-6mdiik2q7ys3fynp7ehx06",
   "model":"llama-3.2-3b-instruct",
   "object":"chat.completion",
   "system_fingerprint":"llama-3.2-3b-instruct",
   "usage":{
      "completion_tokens":17,
      "prompt_tokens":240,
      "total_tokens":257
   }
}
```

### RAG API --> LM Studio
* Request
```
{
   "model":"llm",
   "messages":[
      {
         "role":"system",
         "content":"You are a useful assistant."
      },
      {
         "role":"user",
         "content":" You are an AI thai language model assistant.
                     Answer the question based ONLY on the following context.
                     ข้าวซอยเป็นอาหารเหนือที่มีเอกลักษณ์ ใช้เส้นบะหมี่ไข่ในน้ำแกงกะทิเข้มข้น ใส่เนื้อไก่หรือเนื้อวัว โรยหน้าด้วยบะหมี่ทอดกรอบ เสิร์ฟพร้อมหอมแดงดอง มะนาว และผักดอง;
                     ส้มตำเป็นอาหารอีสานยอดนิยม ทำจากมะละกอดิบขูดฝอย คลุกเคล้ากับน้ำปลา มะนาว พริก กระเทียม มะเขือเทศ และถั่วฝักยาว ให้รสจัดจ้าน เปรี้ยว เผ็ด เค็มและหวานเล็กน้อย
                     Original question: อาหารเหนือมีอะไรบ้าง "
      }
   ]
}
```

* Response
```
{
   "id":"chatcmpl-uyti5avhnlf38be58kqy5",
   "object":"chat.completion",
   "created":1745069487,
   "model":"llama-3.2-3b-instruct",
   "choices":[
      {
         "index":0,
         "logprobs":"None",
         "finish_reason":"stop",
         "message":{
            "role":"assistant",
            "content":"ข้าวซอยเป็นอาหารเหนือที่มีเอกลักษณ์"
         }
      }
   ],
   "usage":{
      "prompt_tokens":240,
      "completion_tokens":22,
      "total_tokens":262
   },
   "system_fingerprint":"llama-3.2-3b-instruct"
}
```
