import pandas as pd
import random
from sklearn.ensemble import RandomForestRegressor  # Zmieniamy model na Las Losowy
from sklearn.model_selection import train_test_split

def generate_data():
    """Generuje dane do nauki: Ilość, Cena i wynikowa Wartość"""
    products = ['Laptop', 'Myszka', 'Klawiatura', 'Monitor']
    data = []
    # Zwiększamy liczbę próbek z 100 do 10000.
    # Random Forest potrzebuje gęstych danych, aby dobrze przybliżyć mnożenie.
    for _ in range(10000):
        prod = random.choice(products)
        qty = random.randint(1, 50)
        price = random.randint(50, 2000)
        # Wartość to wynik mnożenia, ale model ML musi się tego "nauczyć" sam
        total = qty * price 
        data.append({'Ilość': qty, 'Cena_jedn': price, 'Wartość_całkowita': total})
    return pd.DataFrame(data)

def run_ml_example():
    print("--- Prosty przykład Machine Learning (Random Forest) ---")
    
    # 1. Przygotowanie danych
    df = generate_data()
    print(f"Wygenerowano {len(df)} rekordów danych treningowych.")

    # 2. Wybór cech (X) i celu (y)
    # X = dane wejściowe (Ilość, Cena)
    # y = to co chcemy przewidzieć (Wartość całkowita)
    X = df[['Ilość', 'Cena_jedn']]
    y = df['Wartość_całkowita']

    # 3. Podział na zbiór treningowy i testowy (80% nauka, 20% sprawdzian)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 4. Trenowanie modelu
    # Zmieniamy LinearRegression na RandomForestRegressor.
    # Drzewa decyzyjne znacznie lepiej radzą sobie z zależnościami typu mnożenie.
    model = RandomForestRegressor(n_estimators=200, random_state=42)
    model.fit(X_train, y_train)
    print("Model został wytrenowany.")

    # 5. Ocena modelu (R^2 score: 1.0 to idealne dopasowanie)
    score = model.score(X_test, y_test)
    print(f"Dokładność modelu (R^2): {score:.4f}")

    # 6. Przykładowa predykcja dla nowych danych
    new_qty = 10
    new_price = 300
    
    # Tworzymy DataFrame z nazwami kolumn, aby uniknąć ostrzeżenia
    new_data = pd.DataFrame([[new_qty, new_price]], columns=['Ilość', 'Cena_jedn'])
    prediction = model.predict(new_data)[0]

    print(f"\nTest: Ile kosztuje {new_qty} sztuk po {new_price} PLN?")
    print(f" -> Model ML przewiduje: {prediction:.2f} PLN")
    print(f" -> Matematyka mówi:     {new_qty * new_price} PLN")
    print(f" -> Błąd:                {abs(prediction - (new_qty * new_price)):.2f} PLN")

if __name__ == "__main__":
    run_ml_example()
