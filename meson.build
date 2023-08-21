project('libpardus',
	version:'0.0.1',
	license:'GPL3'
)
sources = run_command('find','src','-type','f',check:true).stdout().strip().split('\n')
install_data(sources,install_dir:'/usr/lib/python3/dist-packages/libpardus/')

