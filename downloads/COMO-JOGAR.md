# Horizon com perfis offline — Linux x86_64

Versão não oficial baseada em [horizon-rust/horizon](https://github.com/horizon-rust/horizon),
com a alteração `34ead8e` para perfis locais. O pacote contém os executáveis de desenvolvimento
(perfil Cargo `debug`) e o código-fonte completo. Não contém recursos, jars, mundos ou dados do
Minecraft, nem contas ou tokens. Preserve `LICENSE` e os avisos de terceiros.

## O que baixar

- `horizon-offline-linux-x86_64-debug.tar.gz`: código e executáveis já compilados.
- `horizon-offline-profiles-source.zip`: somente código, para quem quiser compilar.
- `SHA256SUMS`: hashes para conferir os downloads.

Os executáveis são para Linux x86_64, com glibc 2.39 ou superior. A compilação e os testes foram
verificados em Debian 13; não houve teste interativo da interface ou de um mundo. O pacote
`debug` não é otimizado para desempenho. Os testes de inicialização do launcher usam um processo
de prova; isso não equivale a uma partida executada.

## 1. Dependências no Arch Linux

```bash
sudo pacman -Syu --needed alsa-lib systemd-libs libxkbcommon libxkbcommon-x11 \
  libxcb libx11 wayland fontconfig vulkan-icd-loader jdk-openjdk
```

Use JDK 25 ou mais recente. Mantenha instalado o driver gráfico apropriado para sua GPU.

## 2. Extrair o pacote com executáveis

No diretório em que salvou o download:

```bash
tar -xzf horizon-offline-linux-x86_64-debug.tar.gz
cd horizon-offline-linux-x86_64
```

Não execute o jogo com `sudo`.

## 3. Preparar os recursos da sua cópia do Minecraft

Você precisa ter os arquivos de Minecraft: Java Edition **26.3**, a versão fixada por este
checkout, e o server jar correspondente. Instale e abra essa versão uma vez no seu launcher
habitual para que os arquivos e os assets estejam completos. O server jar deve ser obtido pelo
próprio usuário da fonte oficial e deve corresponder a essa versão.

Supondo que seu Minecraft esteja em `~/.minecraft` e o server jar em `~/Downloads/server.jar`:

```bash
./horizon-prepare --prepare --root "$PWD" \
  --minecraft-dir "$HOME/.minecraft" \
  --server-jar "$HOME/Downloads/server.jar"
./horizon-prepare sounds --root "$PWD" --minecraft-dir "$HOME/.minecraft"
```

Se usa Prism ou outro launcher, substitua o caminho pelo diretório da sua instalação. O
preparador verifica os checksums e gera `.local/horizon-client/26.3/`. Não compartilhe essa pasta.
A cópia dos sons é opcional; se falhar, o jogo fica sem som. O preparador não baixa Minecraft.

## 4. Criar o perfil e jogar sem login

Na pasta extraída:

```bash
export HORIZON_HOME="$PWD/meus-dados"
export HORIZON_LAUNCHER_HOME="$PWD/meus-perfis"
./horizon-launcher account offline Builder_1
./horizon-launcher account list
./horizon-client --offline --name Builder_1 \
  --resources "$PWD/.local/horizon-client/26.3"
```

Substitua `Builder_1` pelo nome desejado: de 3 a 16 letras ASCII, números ou `_`. Use o nome com
a mesma grafia no comando do cliente. O launcher salva o perfil em `meus-perfis/accounts.json`;
o UUID é derivado de `OfflinePlayer:<nome>`, conforme a convenção do Minecraft. Nenhum token é
fabricado. Os mundos ficam em `meus-dados`; preserve essas pastas ao trocar de pacote.

O cliente abre o menu inicial. Escolha Singleplayer para criar ou abrir um mundo. Você também
pode abrir a interface do launcher com `./horizon-launcher`, mas a instalação e o botão Play
dessa interface gerenciam as versões que ela instala separadamente. Os comandos acima executam
diretamente o cliente incluído neste pacote.

Perfis offline não autenticam em servidores que exigem uma conta original. Nenhuma verificação
ou configuração de servidores externos foi alterada. O login Microsoft permanece no código;
esta compilação local não inclui um registro de aplicativo Microsoft próprio. Para esse login,
é necessário configurar `HORIZON_MSA_CLIENT_ID`, como no projeto original. Isso não é necessário
para os comandos offline acima.

## Compilar uma versão otimizada a partir do código

Opcional: na raiz do código extraído, instale também as ferramentas de desenvolvimento:

```bash
sudo pacman -S --needed base-devel rust clang lld pkgconf freetype2 vulkan-headers openssl python
cargo build --locked --profile fast -p horizon-client -p horizon-prepare \
  --bin horizon-client --bin horizon-prepare
cargo build --locked --release --manifest-path launcher/Cargo.toml
```

Use então `./target/fast/horizon-client` e `./target/fast/horizon-prepare` no lugar dos executáveis
da raiz, e `./launcher/target/release/horizon-launcher` para o launcher. Os builds verificados
nesta entrega foram os de desenvolvimento; os comandos acima descrevem a compilação otimizada.
