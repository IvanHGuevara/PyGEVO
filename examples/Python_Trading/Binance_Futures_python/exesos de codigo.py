if r_alerta_hora_ant[0].text != r_alerta_hora[0].text:
    r_alerta_hora_ant = r_alerta_hora
    # xpath_alerta = "//div[@class='cellWrap-7p9xAppS apply-overflow-tooltip apply-overflow-tooltip--allow-text']"
    # xpath_alerta = "//div[@class='content-3u7RsyPo']" //p[@class='content-3iANOEPW']
    xpath_alerta = "//div[@class='item-2FogpcK6 item-Ui52k2Oz'][1]/div[@class='message-31pJNocm']"

    element_present = EC.presence_of_element_located((By.XPATH, xpath_alerta))
    WebDriverWait(BROWSER, 99999999999999999999).until(element_present)
    r_alerta = BROWSER.find_elements_by_xpath(xpath_alerta)
    print("")
    print(
        "----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    accion = ""
    if r_alerta[0].text.find("message_long_exit") > 0:
        print("Alerta Close BUY: ")
        accion = "Alerta Close BUY: "
        # cancelarTodasOperaciones()

    if r_alerta[0].text.find("message_short_exit") > 0:
        print("Alerta Close SELL: ")
        accion = "Alerta Close SELL: "
        # cancelarTodasOperaciones()
    if r_alerta[0].text.find("message_long_entry") > 0:
        print("Alerta BUY: ")
        accion = "Alerta BUY: "
        # compraFuturos()
    if r_alerta[0].text.find("message_short_entry") > 0:
        print("Alerta SELL: ")
        accion = "Alerta SELL: "
        # venderFuturos()

    for a in r_alerta[1:]:
        print(str(a.text))
        logging.info(str(datetime.now())[:-7] + ": " + accion + str(a.text))
    time.sleep(0)

    xpath_alerta = "//div[@class='item-2FogpcK6 item-Ui52k2Oz'][2]/div[@class='attributes-2xcuCWOT']/span[@class='attribute-1y6aeCNf']"
    element_present = EC.presence_of_element_located((By.XPATH, xpath_alerta))
    WebDriverWait(BROWSER, 99999999999999999999).until(element_present)
    r_alerta_hora2 = BROWSER.find_elements_by_xpath(xpath_alerta)

    if r_alerta_hora2[0].text == r_alerta_hora[0].text:

        # xpath_alerta = "//div[@class='cellWrap-7p9xAppS apply-overflow-tooltip apply-overflow-tooltip--allow-text']"
        # xpath_alerta = "//div[@class='content-3u7RsyPo']" //p[@class='content-3iANOEPW']
        xpath_alerta = "//div[@class='item-2FogpcK6 item-Ui52k2Oz'][2]/div[@class='message-31pJNocm']"

        element_present = EC.presence_of_element_located((By.XPATH, xpath_alerta))
        WebDriverWait(BROWSER, 99999999999999999999).until(element_present)
        r_alerta = BROWSER.find_elements_by_xpath(xpath_alerta)
        print("")
        print(
            "----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        accion = ""
        if r_alerta[0].text.find("message_long_exit") > 0:
            print("Alerta Close BUY: ")
            accion = "Alerta Close BUY: "
            # cancelarTodasOperaciones()

        if r_alerta[0].text.find("message_short_exit") > 0:
            print("Alerta Close SELL: ")
            accion = "Alerta Close SELL: "
            # cancelarTodasOperaciones()
        if r_alerta[0].text.find("message_long_entry") > 0:
            print("Alerta BUY: ")
            accion = "Alerta BUY: "
            # compraFuturos()
        if r_alerta[0].text.find("message_short_entry") > 0:
            print("Alerta SELL: ")
            accion = "Alerta SELL: "
            # venderFuturos()
    for a in r_alerta[1:]:
        print(str(a.text))
        logging.info(str(datetime.now())[:-7] + ": " + accion + str(a.text))
    time.sleep(0)