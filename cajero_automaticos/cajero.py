class CuentaBancaria:
    def __init__(self, saldo_inicial=0):
        # Corrección: '__init__' con 'i' antes de la 't'
        self.__saldo = saldo_inicial

    def consultar_saldo(self):
        return self.__saldo

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            return True
        return False

    def retirar(self, monto):
        if 0 < monto <= self.__saldo:
            self.__saldo -= monto
            return True
        return False


class CajeroAutomatico:
    def __init__(self, cuenta):
        self.cuenta = cuenta

    def mostrar_menu(self):
        print("\n--- 🏦 SIMULADOR DE CAJERO AUTOMÁTICO ---")
        print("1. Consultar Saldo")
        print("2. Depositar Dinero")
        print("3. Retirar Dinero")
        print("4. Salir")
        
    def iniciar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Selecciona una opción (1-4): ")

            if opcion == "1":
                saldo = self.cuenta.consultar_saldo()
                print(f"💰 Tu saldo actual es: ${saldo}")
                
            elif opcion == "2":
                monto = float(input("Monto a depositar: $"))
                if self.cuenta.depositar(monto):
                    print("✅ Depósito exitoso.")
                else:
                    print("❌ Error: El monto debe ser mayor a 0.")
                    
            elif opcion == "3":
                monto = float(input("Monto a retirar: $"))
                if self.cuenta.retirar(monto):
                    print("✅ Retiro exitoso. Retira tu dinero.")
                else:
                    print("❌ Error: Fondos insuficientes o monto inválido.")
                    
            elif opcion == "4":
                print("👋 Gracias por usar el cajero. ¡Hasta luego!")
                break
            else:
                print("⚠️ Opción no válida. Intenta de nuevo.")


# --- AQUÍ CONECTAMOS TODO (El bloque principal) ---
if __name__ == "__main__":
    # 1. Creamos la cuenta con un saldo inicial de $500
    mi_cuenta = CuentaBancaria(500)
    
    # 2. Le pasamos esa cuenta al cajero (Inyección de dependencia)
    mi_cajero = CajeroAutomatico(mi_cuenta)
    
    # 3. Encendemos el cajero
    mi_cajero.iniciar()