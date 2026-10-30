# Veinminer + Tree Capitator (Rust)

Este mod ativa as duas funções com **Shift esquerdo (agachar)**:

- **Minérios:** quebra a veia conectada do mesmo grupo, incluindo vizinhos diagonais.
- **Árvores:** quebra os troncos/madeiras conectados da mesma espécie; inclui madeira descascada e troncos/hifas do Nether.
- **Sem Shift:** a mineração continua normal.
- Funciona apenas em sobrevivência; cada bloco extra passa pela rotina normal de mineração do Horizon, preservando drops, XP, desgaste e eventos.
- Limite de 100 blocos por operação, busca local limitada e intervalo de segurança entre ativações.
- Folhas não são removidas.

## Gerar o arquivo .hnmod

Na raiz deste repositório:

```bash
python3 mods/veinminer/package.py
```

O arquivo será criado em `target/veinminer-0.1.0.hnmod`. **Não descompacte o .hnmod.**

Copie-o para a pasta `mods/` ao lado do `horizon-launcher` (a mesma pasta em que ficam os outros arquivos .hnmod) e clique em **Jogar**. O launcher compila a combinação de mods na primeira execução e reutiliza o cache nas próximas.

## Compatibilidade

Feito especificamente para o snapshot usado pela release `offline-cinco-mods-v0.2.1`:
- Horizon: `e4472a7423da0740c881132d61e8e9b368bfef4c`
- Horizon Mixins: `d9c83d7096b7ea5b83678da2efdfd6161f74997e`
- Minecraft Java: 26.3

Não use este pacote com outra revisão do Horizon. O pacote contém código Rust nativo, não um JAR Java; revise o código antes de confiar nele. A compilação nativa executa com as permissões da sua conta.

## Limites de validação

O pacote é uma adaptação da lógica de mineração conectada para a revisão fixada neste repositório. A geração do .hnmod não equivale a compilar o cliente: a compilação real ocorre no launcher ao montar a combinação de mods. Faça backup do mundo antes do primeiro teste.
