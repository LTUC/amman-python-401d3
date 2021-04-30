# NVM
if [ -f $(brew --prefix nvm)/nvm.sh ]; then
  source $(brew --prefix nvm)/nvm.sh
fi

if [ -f $(brew --prefix nvm)/etc/bash_completion.d/nvm ]; then
   source $(brew --prefix nvm)/etc/bash_completion.d/nvm
fi

# Python
if command -v pyenv 1>/dev/null 2>&1; then
  eval "$(pyenv init -)"
fi
