#calculadora de consumo de energia

#entrada de dados
aparelho = input("Nome do aparelho:")
potencia = float(input("Potência do aparelho em watts: "))
horas_dia = float(input("Horas de uso por dia: "))

#calculo do consumo mensal (kwh)
consumo_mensal = (potencia*horas_dia*30)/1000

#calculo de custo
custo_kwh = 0.75
custo_estimado = consumo_mensal*custo_kwh

#saida
print("\n--- Resultado ---")
print(f"Aparelho: {aparelho}")
print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")
print(f"Custo estimado: R$ {custo_estimado:.2f}")