---
title: FastEcho
---
<p class="eyebrow">PROJEKT 02 / ACCESSIBILITY / HACKYEAH 2026</p>
# FastEcho

<p class="lead">Powiedz, czego potrzebujesz. Usłysz, co wydarzyło się na stronie.</p>

[Repozytorium ↗](https://github.com/llama-lovers/FastEcho){ .button }
[Zobacz demo ↗](https://youtu.be/zODavr68b5s){ .button .secondary }

## Problem

Czytniki ekranu pozwalają korzystać z internetu, ale znalezienie właściwej kontrolki bywa czasochłonne. Nieopisane przyciski, złożone formularze i dynamiczne menu dokładają kolejne bariery.

## Nasze podejście

FastEcho to rozszerzenie Chrome dla osób niewidomych i słabowidzących. Rozumie polskie polecenia, analizuje strukturę i dostępne etykiety strony, wykonuje zweryfikowane akcje i opisuje zaobserwowany wynik. Odpowiedzi przekazuje przez czytnik ekranu lub lokalny głos Piper.

<div class="quote-panel"><span class="eyebrow">JEDNA ROZMOWA, KONKRETNY REZULTAT</span><p>„Co mogę zrobić?”<br>„Sprawdź status przesyłki.”<br>„Powtórz.”</p><span>Rozpoczęcie i wysłanie nagrania: <kbd>Alt</kbd> + <kbd>Shift</kbd> + <kbd>A</kbd></span></div>

## Co potrafi prototyp

- Opisać bieżącą stronę i zaproponować dostępne działania.
- Kliknąć kontrolkę, wypełnić zwykłe pole formularza i przewinąć stronę.
- Sprawdzić cel przed wykonaniem akcji oraz porównać stan strony po niej.
- Powtórzyć odpowiedź, zmienić jej szczegółowość i obsłużyć potwierdzenie.
- Współpracować z czytnikiem ekranu, lokalnym Piperem i awaryjnym Chrome TTS.

## Architektura i prywatność

Rozszerzenie Manifest V3 współpracuje z lokalnym backendem FastAPI. Rozpoznawanie mowy i wnioskowanie w pełnym trybie korzystają z OpenRouter. Piper syntetyzuje odpowiedzi lokalnie.

Rozpoznane dane wrażliwe są maskowane w kontekście strony. Rozszerzenie odmawia akcji na chronionych polach i rozpoznanych CAPTCHA. Maskowanie jest heurystyką, nie pełną gwarancją. **Nagranie w trybie rzeczywistej transkrypcji trafia do OpenRouter przed maskowaniem tekstu** — nie należy dyktować haseł ani sekretów.

## Wypróbuj

[README FastEcho](https://github.com/llama-lovers/FastEcho#quick-start) zawiera wymagania, budowę rozszerzenia, uruchomienie backendu, lokalną stronę demo i konfigurację Pipera.

Źródło: [repozytorium i dokumentacja FastEcho](https://github.com/llama-lovers/FastEcho).
