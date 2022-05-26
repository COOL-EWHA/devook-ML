# devook-ML
devook의 카테고리 자동분류 머신러닝 API 서버입니다.

<br />

# 🛠 기술 스택
<div> 
  <img src="https://img.shields.io/badge/Python-1572B6?style=for-the-badge&logo=python&logoColor=white"> 
  <img src="https://img.shields.io/badge/Django-61DAFB?style=for-the-badge&logo=django&logoColor=black">
  <img src="https://img.shields.io/badge/Docker-3178C6?style=for-the-badge&logo=docker&logoColor=white">
  <img src="https://img.shields.io/badge/AWS-E34F26?style=for-the-badge&logo=&logoColor=white">    
  <img src="https://img.shields.io/badge/Nginx-2C8EBB?style=for-the-badge&logo=nginx&logoColor=white"> 
  <img src="https://img.shields.io/badge/pykomoran-DB7093?style=for-the-badge&logo=pykomoran&logoColor=white">
  <img src="https://img.shields.io/badge/nltk-FF4154?style=for-the-badge&logo=nltk&logoColor=white">  
  <img src="https://img.shields.io/badge/Fasttext-4B32C3?style=for-the-badge&logo=fasttext&logoColor=white"> 
  <img src="https://img.shields.io/badge/pylint-F7B932?style=for-the-badge&logo=pylint&logoColor=black">
</div>

<br />

# ⚙️ 구조
<img width="809" alt="image" src="https://user-images.githubusercontent.com/69254943/170506011-91330e6a-0269-44d9-8386-186b02ab2dc7.png">

1. 백엔드 서버에서 title 데이터를 전송합니다.
2. Pykomoran과 NLTK 라이브러리를 사용해 전송된 title 데이터를 전처리하고, FastText 모델에 입력값으로 전달합니다.
3. 출력된 카테고리를 반환합니다.
