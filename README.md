# ServeRest - Projeto de Testes de QA  

Projeto de testes de login da aplicação **ServeRest**, utilizando casos de teste em **Gherkin** e automação com **Python, Selenium e Pytest**.  
Desenvolvido como parte da minha prática em automação de testes e estudo de aplicações web.

---

## 🎯 Objetivo do projeto  
Desenvolver casos de teste e automação para o processo de **login** no ServeRest.  
O objetivo foi praticar automação de interface com Selenium, organizar o projeto de forma modular, estruturar cenários em Gherkin e reforçar boas práticas de QA.

---

## 📌 Funcionalidades testadas  

### Casos de teste em Gherkin  
- Login com credenciais válidas  
- Login com credenciais não cadastradas  
- Login com e-mail inválido  
- Validação de campos obrigatórios  
- Exibição de mensagens de erro  

### Automação  
- Login com credenciais válidas  
- Login com senha incorreta  

Os cenários estão documentados no arquivo **Gherkin ServeRest – Casos de teste.pdf**.

---

## ✅ Resultado  
Os testes automatizam o fluxo de login do ServeRest, validando tanto cenários positivos quanto negativos.  
Com eles, é possível garantir que:

- Usuários válidos conseguem acessar a aplicação  
- Credenciais incorretas exibem as mensagens de erro corretas  
- Campos obrigatórios são validados  
- Mensagens de feedback aparecem corretamente na interface  

O projeto utiliza ferramentas e técnicas que mantêm o código limpo, reutilizável e de fácil manutenção.

## 🧪 Exemplo de automação com Selenium  

```python
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions 
from selenium.webdriver.support.wait import WebDriverWait 
 
class ServeRestPage: 
 
    email_field = (By.ID, 'email') 
    password_field = (By.ID, 'password') 
    enter_button = (By.XPATH, '//button.contains(text(),"Entrar")]') 
    initial_page = (By.XPATH, '//h1[contains(text(), "Serverest Store")]') 
    error_message = (By.XPATH, '//span[contains(text(), "Email e/ou senha inválidos")]') 
 
    def __init__(self, driver): 
        self.driver = driver 
 
    def _wait_for_visible(self, locator): 
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(locator)
        ) 
 
    def set_enter(self): 
        self.driver.find_element(*self.enter_button).click() 
 
    def set_login(self, email, password): 
        self.driver.find_element(*self.email_field).send_keys(email) 
        self.driver.find_element(*self.password_field).send_keys(password) 
        self.set_enter()

```

### Testes realizados  
- Validar login com sucesso  
- Validar erro de senha incorreta  
- Validar erro de e-mail inválido  
- Validar campo obrigatório de e-mail  
- Validar campo obrigatório de senha  
- Validar mensagens exibidas no retorno da API  

---

## 🛠 Ferramentas utilizadas  
- **BDD:** Gherkin  
- **Python**  
- **Selenium**  
- **Pytest**  
- **Page Object Model (POM)**  
- **Git e GitHub**  

---

## 🧩 O que eu aprendi  
- Estruturar um projeto de automação com foco em organização e manutenção  
- Criar e validar diferentes cenários de login  
- Implementar métodos reutilizáveis usando POM  
- Trabalhar com tempos de espera e estabilidade dos testes  
- Documentar cenários em BDD  
- Versionar, organizar e apresentar o projeto no GitHub  

---

## Como executar este projeto

### 1. Clone o repositório
```bash
git clone <URL_DO_REPOSITORIO>
```
### 2. Acesse a pasta
```bash
cd Login_ServeRest
```
### 3. Crie o ambiente virtual
```bash
python -m venv venv
```
### 4. Ative o ambiente virtual

Windows:
```bash
venv\Scripts\activate
```
Mac/Linux:
```bash
source venv/bin/activate
```
### 5. Instale as dependências
```bash
pip install -r requirements.txt
```
### 6. Execute os testes
```bash
pytest -v
```