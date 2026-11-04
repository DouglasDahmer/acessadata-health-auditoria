# Procedimento de publicação — GitHub Pages

## 1. Criar uma cópia isolada

Extraia este pacote para uma pasta nova, **separada do diretório privado da pesquisa**. Não copie o diretório completo da pesquisa: ele contém arquivos brutos, temporários e evidências que precisam de revisão individual antes de distribuição.

## 2. Inspecionar e validar

No PowerShell dentro da pasta extraída:

```powershell
Rscript .\scripts\verificar_agregados.R
python .\scripts\verificar_agregados.py
quarto --version
quarto render
New-Item -ItemType File -Path .\docs\.nojekyll -Force | Out-Null
```

Se o comando `quarto` não existir, instale-o a partir de https://quarto.org/docs/get-started/. Se houver erro referente a `knitr`, instale-o no R em uso (por exemplo `Rscript -e "install.packages('knitr', repos='https://cloud.r-project.org')"`).

## 3. Revisão pré-publicação

- Confira se os números e a descrição do estudo correspondem às versões que você deseja divulgar.
- Revise links e referências oficiais.
- Verifique se **não há microdados, dados pessoais, tokens, históricos de terminal, senhas, ZIPs originais ou planilhas brutas**.
- Não publique código de biblioteca privada (incluindo AdVeri) sem decidir a licença e os direitos aplicáveis.
- Preserve as ressalvas metodológicas e o caráter preliminar do estudo.

## 4. Inicialização de repositório separado

Crie um repositório vazio no GitHub, por exemplo `acessadata-health-auditoria`. Na pasta de publicação:

```powershell
git init
git branch -M main
git add .
git status --short
# Revise os arquivos acima antes de continuar.
git commit -m "Publica auditoria computacional do AcessaData-Health"
git remote add origin https://github.com/SEU_USUARIO/acessadata-health-auditoria.git
git push -u origin main
```

Os comandos `git remote`/`push` são exemplos — ajuste o usuário e o repositório. A publicação remota **não ocorre** automaticamente ao extrair este pacote.

## 5. Ativar GitHub Pages

No repositório GitHub, entre em **Settings → Pages → Build and deployment**. Selecione **Deploy from a branch**, escolha `main` e `/docs`, e salve. Aguarde o serviço indicar o endereço publicado, normalmente `https://SEU_USUARIO.github.io/acessadata-health-auditoria/`.

O método de saída em `docs/` segue a documentação oficial do Quarto: https://quarto.org/docs/publishing/github-pages.html

## 6. Etapas posteriores

Quando a demonstração estiver publicada e revisada, poderá ser ampliada com código do pipeline integral de extração, testes automatizados em CI, relatórios científicos adicionais e um dashboard epidemiológico. Cada etapa deverá ter seu próprio escopo, testes e evidências.
