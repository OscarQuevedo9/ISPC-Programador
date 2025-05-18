def ejecutar_automatizacion(dispositivos):
    print("\nEjecutando Modo Ahorro de Energía...")
    for d in dispositivos:
        if d['tipo'].lower() != "cámara": 
            d['estado'] = "apagado"
    print("Dispositivos no esenciales apagados.")