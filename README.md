# AP1VS Závěrečný týmový projekt
Repozitář závěrečného týmového projektu v předmětu Nástroje pro vývoj softwarových projektů (zkratka AP1VS) na [Fakultě aplikované informatiky Univerzity Tomáše Bati ve Zlíně](https://fai.utb.cz/).

## Zadání projektu
Program pro zjištění informací o trojúhelníku se zadanými vrcholy.

### Vstup
- Souřadnice vrcholů (tří bodů) ve 2D prostoru
- Program musí mít implementovánu alespoň jednu z následujících možností zadávání souřadnic:
  - Předávání souřadnic pomocí parametrů při spuštění, nebo
  - Zadávání souřadnic za běhu programu dotazováním uživatele

### Výstup
- Informace, zda je trojúhelník možné sestrojit
- Informace o délkách stran trojúhelníku
- Informace o obvodu a obsahu trojúhelníku
- Informace, zda je trojúhelník pravoúhlý

### Další požadavky na zpracování
- Je třeba využít některého nástroje pro řízení projektu (využito [Trello](https://trello.com) pro svou jednoduchost)
- Veškerý kód musí být řádně zdokumentován
- Použití některého generátoru dokumentace (využito [Sphinx](https://www.sphinx-doc.org/en/master/))
- Ke kódu by měly být vytvořeny Unit testy

## Spuštění programu

### Se zadáváním souřadnic za běhu programu
```console
python main.py
```
Program po spuštění tímto způsobem očekává zadání souřadnic ke každému ze tří vrcholů trojúhelníku.
U každého z vrcholů očekává vstup složený ze dvou čísel oddělených mezerou.

### S předáním souřadnic při spuštění
```console
python main.py <Ax> <Ay> <Bx> <By> <Cx> <Cy>
```

## Vygenerování dokumentace
Zdrojové soubory generátoru Sphinx jsou uloženy v podadresáři `/docs/`.
Uvnitř tohoto adresáře je třeba spustit následující příkaz:
```console
make html
```
Cesta k úvodní stránce vygenerované dokumentace je pak `/docs/_build/html/index.html`.

## Omezení a možná rozšíření programu

### Omezení
- Program byl navržen s předpokladem, že uživatel zná pouze souřadnice bodů tvořící trojúhelník, není tedy implementována funkce pro zjištění vlastností trojúhelníku zadaného jinak, než třemi vrcholy.

### Možná  rozšíření
- Zjištění dalších vlastností trojúhelníku, jako jsou jeho výšky, vnitřní úhly a další.
- Rozšíření o další geometické útvary mimo trojúhelník, které je možné zadat prostřednictvím vrcholů.
