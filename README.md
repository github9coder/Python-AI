# Python-AI
  This ai talks about python, and only about python.
![python_ai](https://github.com/github9coder/Python-AI/assets/130998051/04ce1b83-d53d-423c-a14b-0c3d065e9b1b)
  - - -
## Description:
  This artificial intelligence should be used __to learn, and create projects on python.__
You can create a new one, __replacing the API key by your own__, by creating an account at <https://platform.openai.com>, and on the left-hand menu, clicking on "_API keys_", and creating a secret key, and replacing it on
```python
    client = \
        OpenAI(api_key= YOUR_API_KEY_GOES_HERE
               )
    OpenAI.api_key = os.getenv('OPENAI_API_KEY')
```

To modify its behavoiur, change the content to whatever you want on:

```python
        conversation =  [
                    {'role': 'system',
                    'content': Your content goes here.
                    {'role': 'user', 'content': user_input}
                    ]
```

This artificial intelligence has been coded with openai, and after creating it, I have used it to develop itself.
- - -

This AI uses the openai package at @[OpenAI github's page](https://github.com/openai/openai-python)

- - -
