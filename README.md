# dizge

![Sürüm](https://img.shields.io/pypi/v/dizge?style=flat-square)
![Lisans](https://img.shields.io/pypi/l/dizge?style=flat-square)

import dizge

## Giriş
**dizge**, [diLab](http://dilab.ankara.edu.tr/) DDİ çalışma grubu (Mehmet Umut Mutlu, Nazlıcan Yetimaslan, İlker Atagün) tarafından Python için geliştirilen Türkçe dilbilim analiz aracıdır. Kütüphanenin içeriği, biri Nesne Tabanlı Programlama (OOP) mantığıyla oluşturulmuş `competence` (edinç) adlı, diğeriyse sesbilimsel süreçlerin kural tabanlı (rule-based) olarak işlendiği `tools` (araçlar) adlı iki temel modülden oluşmaktadır. Aracın bu sürümünde (*v0.1.0*) seslem analizi ve fonetik çevriyazı gibi sesbilimsel fonksiyonlar bulunmaktadır.

**dizge**'nin teorik arkaplanını aşağıdaki kaynaklar oluşturmaktadır:<br/>
- Ergenç, İ. ve Uzun, İ. P. (2020). *Türkçenin ses dizgesi* (2. baskı). Seçkin Yayınevi.<br/>
- IPA Chart, http://www.internationalphoneticassociation.org/content/ipa-chart, available under a Creative Commons Attribution-Sharealike 3.0 Unported License. Copyright © 2018 International Phonetic Association.

Kütüphanemizden yararlandığınız çalışmalarınızda, bizden aşağıdaki gibi söz edebilirsiniz:<br/>
```
Mutlu, M. U., Yetimaslan, N. ve Atagün, İ. (2021). dizge. https://github.com/mehmetumutmutlu/dizge
```

## Nasıl Kullanılır?
### Paketi Yükleme ve Çalıştırma
Kütüphanemizi GitHub üzerinden indirip veya pip aracı yardımıyla (`pip install dizge`) sisteminize kurabilirsiniz. Bunun ardından kütüphaneyi aşağıdaki gibi çalıştırabilirsiniz.

```python
import dizge
```

### Veri Yükleme
**dizge**'de analiz edeceğiniz veri ya *xlsx* veya *csv* gibi tablo tabanlı bir biçimde ya da *txt* gibi düz metin formatında olabilir. Bu veriyi çalışma dizininize eklemek için harici paketler veya Python'ın built-in fonksiyonlarını kullanabilirsiniz, bu tamamen tercihinize bağlıdır. Aşağıda bir örnek kullanım paylaşılmıştır:
```python
data = open('data/sample.txt', 'r', encoding="utf-8").read()
```

Veriyi yukarıdaki gibi yükledikten sonra veri içinde kullanacağınız bölümü çözümleme öncesinde standardize etmeniz gerekmektedir. Bunun için kütüphane içindeki `standardize()` fonksiyonunu kullanmanız gerekir. Şimdi örnek üzerinden anlatalım:
```python
words = dizge.standardize(data)
```

### `competence` Modülü Fonksiyonları
**dizge**'nin içinde Türkçenin ses dizgesine ait bazı bilgiler Nesne Tabanlı Programlama mantığıyla eklenmiştir. Bu bilgilere ulaşım oldukça kolaydır. Örneğin ünlü veya ünsüzlerin dökümünü aşağıdaki gibi bir kod ile alabilirsiniz:
```python
for i in [vars(phoneme) for phoneme in dizge.vowels]:
    print(i)

for i in [vars(phoneme) for phoneme in dixge.consonants]:
    print(i)
```

Aynı zamanda bir sesin, edinçteki özelliklerini sorgulayabileceğiniz fonksiyonlar da `competence` modülü içinde tanımlanmıştır. Bunlar: 
`isVowel()`, `isUnrounded()`, `isRounded()`, `isClose()`, `isCloseMid()`, `isOpenMid()`, `isOpen()`, `isFront()`, `isCentral()`, `isBack()`, `isConsonant()`, `isPlosive()`, `isNasal()`, `isTrill()`, `isTaporFlap()`, `isFricative()`, `isLateralFricative()`, `isApproximant()`, `isLateralApproximant()`, `isBilabial()`, `isLabiodental()`, `isDental()`, `isAlveolar()`, `isPostalveolar()`, `isRetroflex()`, `isPalatal()`, `isVelar()`, `isUvular()`, `isPharyngeal()`, `isGlottal()`, `isVoiced()`, `isVoiceless()`

### `tools` Modülü Fonksiyonları
Bu modülde G2P ve seslem analizi gibi sesbilimsel süreçler ile ilgili bazı fonksiyonlar bulunmaktadır. Bunları yukarıda hazır hale gelirdiğimiz veri üzerinde tek tek yapabileceğimiz gibi bir sonraki başlıkta anlatacağımız çözümleyici aracıyla toplu bir şekilde de yapabilirsiniz.

Türkçede <ğ> yazıbiriminin sesel karşılığının olmaması nedeniyle, bu yazıbirim ünlü kayması, uzama gibi çeşitli görevler üstlenmektedir. Paketimizdeki `softG()` fonksiyonu <ğ> yazıbiriminin gerçekleşme biçimlerini göstermektedir. 

```python
>>> dizge.softG('dağ')
'daː'
>>> dizge.softG('göğüs')
'göːüs'
>>> dizge.softG('eğlence')
'eylence'
```

Bir sözcüğün seslem analizini farklı biçimlerde yapabilirsiniz. Örneğin, ortografi temelli olarak ve herhangi bir önişlem yapmadan gerçekleştirmek istiyorsanız `syllable_o()` fonksiyonunu kullanabilirsiniz.

```python
>>> dizge.syllable_o('afyonkarahisarlılaştıramadıklarımızdanmışçasına')
['af', 'yon', 'ka', 'ra', 'hi', 'sar', 'lı', 'laş', 'tı', 'ra', 'ma', 'dık', 'la', 'rı', 'mız', 'dan', 'mış', 'ça', 'sı', 'na']
```

Seslem analizini fonetik temelli yapmak isterseniz `syllable_p()` fonksiyonunu kullanabilirsiniz.
```python
>>> dizge.syllable_p('afyonkarahisarlılaştıramadıklarımızdanmışçasına')
[('ɑf', 'VC'), ('jɔŋ', 'CVC'), ('kɑ', 'CV'), ('ɾɑ', 'CV'), ('çI', 'CV'), ('sɑɾ', 'CVC'), ('łɨ', 'CV'), ('łɑʃ', 'CVC'), ('tɨ', 'CV'), ('ɾɑ', 'CV'), ('mɑ', 'CV'), ('dɨk', 'CVC'), ('łɑ', 'CV'), ('ɾɨ', 'CV'), ('mɨz', 'CVC'), ('dɑn', 'CVC'), ('mɨʃ', 'CVC'), ('tʃɑ', 'CV'), ('sɨ', 'CV'), ('nɑ', 'CV')]
```

Yukarıdaki analizde hangi seslem örüntüsünden kaç tane olduğunu hesaplamak için `countSyllable()` fonksiyonunu kullanabilirsiniz.
```python
>>> dizge.countSyllable('afyonkarahisarlılaştıramadıklarımızdanmışçasına')
{'VC': 1, 'CVC': 7, 'CV': 12}
```

Kütüphanenin sesbilimsel araştırmalara sunacağını düşündüğümüz en büyük katkı da kararlı bir G2P (grapheme-to-phoneme) fonksiyonu sayesinde çevriyazı sunmasıdır. Bunun için `g2p()` fonksiyonu kullanılabilir.

```python
>>> dizge.g2p('afyonkarahisarlılaştıramadıklarımızdanmışçasına')
'ɑfjɔŋkɑɾɑçIsɑɾłɨłɑʃtɨɾɑmɑdɨkłɑɾɨmɨzdɑnmɨʃtʃɑsɨnɑ'
```

**ÖNEMLİ NOT**
Referanslarımızdan farklı olarak uzamanın iki biçiminden (tam ve yarım uzama) yalnızca tam uzamayı işledik. Önümüzdeki sürüm güncellemelerinde yarım uzamanın da eklenmesi düşünülmektedir. Ayrıca kaynaklarımızda konuşma dili üzerinden sunulan alternatifli çevriyazılar için fonksiyonumuz da alternatif bir çıktı vermektedir. Kullanıcılar istedikleri çıktıyı indexing yöntemi ile seçebilirler.
 
### Analiz ve Çıktı Alma
Bir önceki başlıkta anlatılan araçlardan bir veya birkaçını bir veri seti üzerinde çalıştırıp bütüncül bir çıktı almak için `analyze()` fonksiyonunu kullanabilirsiniz. Bu fonksiyon ilki verinin kendisi, ikincisi de istediğiniz araçların adlarından oluşan bir liste olmak üzere iki zorunlu parametreden oluşmaktadır.

```python
>>> words = ["ankara", "dil", "bilim", "dilbilim"]
>>> result = dizge.analyze(words, ["g2p", "syllable_o", "syllable_p", "countSylable", "harmony"])

```

### Planlanan Güncellemeler
- Kütüphaneyle entegre çalışan bir web servisi
- Sesbilimsel süreçlerle ilgili ek fonksiyonlar
- Biçimbilimsel çözümleyici
