---
title: FastFence
---
<p class="eyebrow">PROJEKT 01 / AI SECURITY / HACKYEAH 2026</p>
# FastFence

<p class="lead">Kontrola nad tym, co agent AI może przeczytać, wysłać i wykonać.</p>

[Dokumentacja ↗](https://fastfence.dev/){ .button }
[Repozytorium ↗](https://github.com/llama-lovers/FastFence){ .button .secondary }
[Prezentacja i demo →](../presentations.md){ .text-link }

## Problem

Agenci AI pracują z modelami, API i narzędziami. Mogą ujawnić poufne informacje, wykonać niedozwoloną operację albo zużyć zbyt wiele zasobów. Rozproszone po aplikacji reguły trudno utrzymać i sprawdzić.

## Nasze podejście

FastFence umieszcza polityki bezpieczeństwa pomiędzy aplikacją a modelami i narzędziami. Łączy szybkie reguły lokalne z analizą semantyczną. W panelu można opisać regułę językiem naturalnym przy pomocy Laya, sprawdzić zmianę, uruchomić testy i aktywować politykę bez restartu.

<div class="feature-grid" markdown>
<div markdown>
### Jedno miejsce na reguły
Kontrola dostępu, dozwolone modele i narzędzia, limity zasobów oraz budżety szacowanych kosztów.
</div>
<div markdown>
### Ochrona i audyt
Wykrywanie danych wrażliwych i sekretów, filtrowanie wzorców ataków oraz oczyszczone zapisy decyzji.
</div>
<div markdown>
### Integracje
Interfejsy REST, zgodność z OpenAI, MCP oraz synchroniczny tekstowy profil ACP.
</div>
<div markdown>
### Sprawdzalne polityki
Konfiguracja YAML, testy reguł, przegląd różnic i panel do obserwowania wyników.
</div>
</div>

## Zobacz pełny scenariusz

Prezentacja pokazuje zmianę polityki, decyzje ochrony, przegląd reguły Laya, przetwarzanie dokumentów i integracje. Materiały końcowe obejmują film oraz dziesięć slajdów.

[Otwórz prezentację PDF ↗](https://github.com/llama-lovers/FastFence/blob/main/presentation/output/fastfence-submission.pdf){ .button .secondary }

## Uruchom lokalnie

Instrukcje instalacji, wymagania i konfigurację znajdziesz w [aktualnej dokumentacji FastFence](https://fastfence.dev/). Projekt rozwijamy otwarcie — kod, przykłady i materiały demonstracyjne są w [repozytorium](https://github.com/llama-lovers/FastFence).

Źródła: [README projektu](https://github.com/llama-lovers/FastFence), [materiały prezentacyjne](https://github.com/llama-lovers/FastFence/tree/main/presentation).
