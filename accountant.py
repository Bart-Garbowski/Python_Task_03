ALLOWED_COMMANDS = ("exit", "konto", "magazyn", "zakup", "saldo", "sprzedaz", "przeglad")
saldo = 1200.0
store = {
    "rower": {"price": 200.0, "count": 3},
    "mleko": {"price": 10.0, "count": 32},
}

operation_history = []

while True:
    print("#"*100)
    print(f"Dozwolne komendy: {ALLOWED_COMMANDS}")
    command = input("Wpisz komendę: ")
    command = command.lower()

    if command not in ALLOWED_COMMANDS:
        print("Niepoprawna komenda!")
        continue

    if command == "exit":
        break

    elif command == "konto":
        print(f"Stan konta: {saldo} PLN")
        msg = f"Sprawdzono stan konta. Stan konta: {saldo}"
        operation_history.append(msg)

    elif command == "magazyn":
        product_name = input("Nazwa towaru: ")

        product_info = store.get(product_name)
        if product_info:
            print(f"Informacje o produkcie: {product_name}")
            print(product_info)
        else:
            print(f"Nie ma towaru '{product_name}' w magazynie!")
        """if product_name in store.keys():
            print(f"Informacje o produkcie: {product_name}")
            print(store[product_name])
        else:
            print(f"Nie ma towaru '{product_name}' w magazynie!")"""
        msg = f"Sprawdzono stan magazynu dla produktu {product_name}."
        operation_history.append(msg)

    elif command == "zakup":
        product_name = input("Nazwa produktu: ")
        price = input("Cena za sztukę: ")
        count = input("Ilość: ")

        price = float(price)
        count = int(count)

        product_total_price = price*count

        if product_total_price > saldo:
            print(f"Za mało środków na koncie ({saldo}) na zakup towarów za cenę {product_total_price}!")
            continue
        else:
            # saldo = saldo - product_total_price
            saldo -= product_total_price
            if product_name in store.keys():
                store[product_name]["price"] = price
                store[product_name]["count"] += count
            else:
                store[product_name] = {"price": price, "count": count}
                msg = f"Zakupiono product {product_name}. Ilosc sztuk: {count}. Za kwote {price} PLN. "
                operation_history.append(msg)

    elif command == "saldo":
        price = input("Kwota zmiany salda: ")
        price = float(price)
        koment = input("Komentarz: ")
        if (saldo + price) >= 0:
            saldo += price
        else:
            print("Brak wystarczających środków na koncie!")
            continue
        msg = f"Operacja na saldzie, nowe saldo po operacji = {saldo}. Komentarz: {koment}. Ile: {price} "
        operation_history.append(msg)

    elif command == "sprzedaz":
        product_name = input("Nazwa produktu: ")

        if product_name not in store:
            print(f"Nie ma takiego produktu w magazynie!")
        else:
            if product_name in store.keys():
                count = input("Ilość: ")
                price = store[product_name]["price"]
                ilosc_w_magazynie = store[product_name]["count"]
                price = float(price)
                count = int(count)

                if count > ilosc_w_magazynie:
                    print(f"Niewystarczajaca ilosc {product_name} w magazynie! ")
                    continue
                total_price = price * count

                saldo += total_price
                if product_name in store.keys():
                    store[product_name]["count"] -= count
                    msg = f"Sprzedano product {product_name}. Ilosc sztuk: {count}. Za kwote {total_price} PLN. "
                    operation_history.append(msg)

    elif command == "przeglad":
        start = input("Od: ")
        end = input("Do: ")
        start = int(start)
        end = int(end)
        for operation in operation_history[start:end]:
            print(operation)
