#!/bin/bash
sudo apt update
sudo apt install -y curl git openssh-client openssh-server jq build-essential python3 python3-pip nodejs npm nginx mysql-server golang-go zsh crunch sqlmap whois sublist3r
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
chsh -s $(which zsh)

# Hunt tools
go install github.com/ffuf/ffuf/v2@latest
go install github.com/ImAyrix/fallparams@latest
go install github.com/tomnomnom/waybackurls@latest
go install -v github.com/tomnomnom/anew@latest
go install github.com/tomnomnom/assetfinder@latest
go install -v github.com/projectdiscovery/mapcidr/cmd/mapcidr@latest
go install github.com/projectdiscovery/katana/cmd/katana@latest
go install -v github.com/projectdiscovery/dnsx/cmd/dnsx@latest
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest
go install github.com/lc/gau/v2/cmd/gau@latest
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
go install -v github.com/projectdiscovery/shuffledns/cmd/shuffledns@latest
go install github.com/ImAyrix/cut-cdn@latest
go install github.com/hakluke/hakrawler@latest
git clone https://github.com/projectdiscovery/nuclei-templates.git
git clone https://github.com/danielmiessler/SecLists.git

# Installing massDNS
git clone https://github.com/blechschmidt/massdns.git
cd massdns
make
sudo cp bin/massdns /usr/local/bin/
cd ..
rm massdns -rf

# Installing x8
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -y
. "$HOME/.cargo/env"
cargo install x8

