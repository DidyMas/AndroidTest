Feature: Prueba de inicio de sesión

Scenario: Usuario accede a la página de inicio de sesión
  Given el navegador está abierto
  When navego a "http://3.136.167.94:3002/signin"
  Then el título de la página debería ser "App MX"