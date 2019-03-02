# MSR-CNN
  (English)The implementation of Mongolian Speech Recognition using tensorflow and flask
  
  (Монгол)Монгол хэл дээрх Яриа боловсруулагчийг Tensorflow болон Flask ашиглан хэрэгжүүлэв

# Objective ||| Зорилго
  (English)To develop the system using the model learnt on database based on recordings of 600 people telling numbers between 0 - 9 (10 seconds per each person)

  For the training, We used 'Convolutional Neural Networks for Small-footprint Keyword Spotting' (http://www.isca-speech.org/archive/interspeech_2015/papers/i15_1478.pdf) architecture.
  
  
  (Монгол)Энэхүү репо нь 600 гаруй хүний Монгол хэл дээр тэгээс есийн хооронд (0-9) хооронд хэлсэн 10 секундийн бичлэгээр сургагдсан моделийг хэрэглээний түвшинд ашиглах систем хөгжүүлэхэд оршино.

  Сургалтын явцад 'Convolutional Neural Networks for Small-footprint Keyword Spotting' (http://www.isca-speech.org/archive/interspeech_2015/papers/i15_1478.pdf) архитектурийг ашигласан болно.

# Installation and Use ||| Ашиглах заавар
  (English)FYI: During the development, python3(.6.5) used and not sure it works in python2. About the browser, Google Chrome was used in testing and Safari is not supported this time.

  (Монгол)Жич: Хөгжүүлэлтийг python3(.6.5) дээр хийсэн ба python2 дээр туршаагүй болно. Browser-ийн хувьд Google Chrome дээр туршсан ба Safari дээр ажиллахгүй болно.
  
    pip3 install -r /path-to-project/requirement.txt
    python3 /path-to-project/app.py
    open index.html
    
# References ||| Ашигласан материал
  
  - http://www.isca-speech.org/archive/interspeech_2015/papers/i15_1478.pdf
  - https://www.tensorflow.org
