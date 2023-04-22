## Povinně implementovaná funkčnost
|  | stav |
| --- | --- |
| generování hodu kostkami | DONE                     |
| výpis všech možných tahů hráče |  |
| jednoduchá umělá inteligence, která náhodně volí jeden z platných tahů | |
| trasování chodu každého jednotlivého kamene (od vstupu z baru po vyhození/vyvedení), herní pole se chovají jako zásobník | |
| uložení a obnova stavu hry (s návrhem vlastního JSON formátu pro uložení) | |

## Displej (výpis na standardním vstupu)
| | stav |
| --- | --- |
| výsledky hodů kostkami | DONE |
| pozice všech kamenů na desce (včetně těch "na baru") | |
| stručný komentář toho, co se ve hře událo a nemusí být zřejmé ze zobrazení na desce (kámen vstoupil do hry, byl "vyhozen", opustil hru, hráč nemůže hrát tj. ani házet, pod.) | |
| počet vyvedených kamenů | |
| po výhře typ výhry | |
| po ukončení se zobrazí statistika o všech kamenech ve hře (zvlášť pro bílého a černého), například: | |
| počet kamenů vyhozených, vyvedených a opuštěných | |
| průměrná životnost kamene v tazích | |

## Implementované třídy
| | stav |
| --- | --- |
| Hra (Herní deska) | | 
| HerníPole (modifikovaný zásobník, lze vkládat jen kameny stejných barev) | |
| Dvojkostka (vrací seznam možných dvojic či čtveřic) | DONE |
| Bar (továrna na herní kameny, s řízenou produkcí)| |
| Herní kámen (s pamětí, kde se postupně nacházel) | |

## Hráč
| | stav |
| --- | --- |
| KonzolovýHráč | |
| AIHráč | |