" To install a package, clone the repo into ~/.vim/pack/plugins/start

set nocompatible " disable vi compatibility
filetype plugin indent on
syntax on
set tabstop=4
set softtabstop=4
set shiftwidth=4
set expandtab

let mapleader = ','
let g:mapleader = ','

" save file with ,w
nmap <leader>w :w!<CR>
" run makefile with ,m
nmap <leader>m :make<CR>

" big-Q goes into ex mode; just disable that
nnoremap Q <Nop>

" pencil-goyo command
function PG ()
    Pencil
    Goyo
endfunction
command PG exec PG ()

" not-weird R indentation
let r_indent_align_args = 0

" italics
set t_ZH=[3m
set t_ZR=[23m

let g:pencil#wrapModeDefault = 'soft'   " default is 'hard'

augroup configgroup
    autocmd!
    " Shortcuts to run scripts
    autocmd FileType python nnoremap <buffer> <leader>r :w!<CR>:!python3 %<CR>
    " autocmd FileType r nnoremap <buffer> <leader>r :w!<CR>:!Rscript %<CR>
    autocmd FileType r nnoremap <buffer> <leader>r :w!<CR>:! Rscript %<CR>
    autocmd FileType r ab 5.5 %>%
    autocmd FileType r setlocal softtabstop=2 tabstop=2 shiftwidth=2
    " In text-like files, j/k go up and down a visual line
    " autocmd FileType markdown nnoremap j gj
    " autocmd FileType markdown nnoremap k gk
    autocmd FileType markdown set linebreak
    " autocmd FileType tsv setlocal softtabstop=20 noexpandtab
    " autocmd FileType yaml setlocal shiftwidth=4 tabstop=4
    autocmd FileType html setlocal shiftwidth=2 tabstop=2 softtabstop=2
    autocmd FileType yaml setlocal shiftwidth=2 tabstop=2 softtabstop=2
    autocmd FileType lua nnoremap <buffer> <leader>r :w!<CR>:!lua %<CR>
    autocmd FileType ruby nnoremap <buffer> <leader>r :w!<CR>:!ruby %<CR>
    autocmd FileType snakemake nnoremap <buffer> <leader>r :w!<CR>:!snakemake<CR>
    " remove trailing whitespace before saving .md files
    autocmd BufWritePre *.md %s/\s\+$//e
augroup END

augroup pandoc_syntax
    au! BufNewFile,BufFilePre,BufRead *.md set filetype=markdown.pandoc
augroup END

augroup r_syntax
    au! BufNewFile,BufFilePre,BufRead .R* set filetype=r
augroup END
