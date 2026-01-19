# Ćwiczenie nr 19 – Pomiar stałej grawitacji G (ważenie Ziemi)

## Uwaga!

Urządzenie do pomiaru stałej grawitacji jest niezwykle delikatne i wrażliwe na wstrząsy. Bardzo cienka i droga nić metalowa, na której zawieszone jest wahadło, może urwać się przy nieostrożnym postępowaniu. Zabrania się studentom podejmowania prób regulacji przyrządu, a nawet jego dotykania. Koszty naprawy pokryje sprawca uszkodzenia.

## I. Wstęp

Siłę oddziaływania grawitacyjnego dwóch ciał o masach \( M_1 \) i \( M_2 \) określa wzór Newtona:

```math
F_g = G \frac{M_1 M_2}{r^2} \tag{1}
```

Dla kul o masie 1 kg oddalonych o 5 cm siła ta wynosi jedynie \( 2.7 \times 10^{-8} \) N — kilka milionów razy mniej niż siła ciężkości. Dokładny pomiar pozwala na wyznaczenie wartości \( G \), a dalej masy Ziemi \( M_Z \) i jej gęstości.

Jedna z metod: waga skręceń Henry’ego Cavendisha (1798). Schemat układu:

- Na cienkiej nici zawieszono pręt z kulkami o masie \( m \).
- W pobliżu umieszczone są większe kule o masie \( M \).
- Pod wpływem sił grawitacyjnych pręt się obraca, a nić skręca się.
- Równowaga zachodzi, gdy moment sił sprężystości równoważy moment sił grawitacyjnych.

Moment sił grawitacyjnych:

```math
N_g = 2F_g d = 2 \cdot \frac{G m M}{r^2} \cdot d \tag{2}
```

Moment sił sprężystości:

```math
N_s = K_s \varphi = \frac{\pi \Gamma \rho^4}{2l} \varphi \tag{3}
```

Równanie ruchu wahadła skrętnego:

```math
J \frac{d^2\varphi}{dt^2} + K_s \varphi = 0 \tag{4}
```

Okres drgań:

```math
T = 2\pi \sqrt{\frac{J}{K_s}} \tag{5}
```

Stąd:

```math
K_s = \frac{4\pi^2 J}{T^2} \tag{6}
```

Dla dwóch kul na pręcie:

```math
J = 2 m d^2 \Rightarrow K_s = \frac{8\pi^2 m d^2}{T^2} \tag{7}
```

## II. Opis eksperymentu

Zamiast czekać na ustalenie położenia równowagi, mierzymy środek oscylacji \( \Delta\varphi \), zmieniając pozycje dużych kul. Plamka światła odbita od zwierciadełka na wahadle pokazuje kąt wychylenia:

```math
\varphi = \frac{\Delta b}{4L} \tag{8}
```

Moment sprężysty:

```math
N_s = K_s \varphi = \frac{8\pi^2 m d^2}{T^2} \cdot \frac{\Delta b}{4L} \tag{9}
```

Porównując z \( N_g \), mamy:

```math
G = \frac{2\pi^2 b d r^2}{L M T^2} \tag{11}
```

## III. Pomiary

1. Obserwuj plamkę po przesunięciu kul przez prowadzącego.
2. Zapisuj położenia co 30 s przez dwa okresy (~30 min), dla dwóch położeń kul.

## IV. Opracowanie wyników

1. Oblicz położenia środkowe wychyleń \( b*{01} \), \( b*{02} \):

```math
b_{01} = \frac{b_1 + 2b_2 + b_3}{4} \tag{12}
```

2. Oblicz \( \Delta b = b*{01} - b*{02} \) i podstaw do wzoru (11).

   - \( M = 1.5\, \text{kg} \)
   - \( d = 0.05\, \text{m} \)
   - \( r = 0.047\, \text{m} \)
   - \( L = 0.86\, \text{m} \)

3. Oszacuj masę Ziemi ze wzoru (1) i porównaj z wartością tablicową \( M_Z = 5.98 \times 10^{24}\, \text{kg} \).

4. Analiza niepewności:

```math
G = A \cdot \frac{\Delta b}{T^2}, \quad A = \frac{2\pi^2 d r^2}{L M}
```

```math
\frac{u(G)}{G} = \frac{u(\Delta b)}{\Delta b} + 2 \cdot \frac{u(T)}{T}
```

## V. Literatura

[1] A. Wróblewski, J. Zakrzewski, _Wstęp do Fizyki_, t. II, cz. 1, PWN 1989.  
[2] H. Szydłowski, _Pracownia Fizyczna_, PWN 1999.

## VI. Zagadnienia do kolokwium

- Prawo ciążenia powszechnego.
- Metody wyznaczania stałej grawitacji, w szczególności metoda Cavendisha.
