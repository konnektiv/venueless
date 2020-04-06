const path = require('path')
const webpack = require('webpack')

module.exports = {
	devServer: {
		host: 'localhost',
		disableHostCheck: true,
		port: 8880
	},
	transpileDependencies: ['buntpapier'],
	configureWebpack: {
		resolve: {
			symlinks: false, // don't flatten symlinks (for npm link)
			modules: [path.resolve('src'), path.resolve('src/styles'), 'node_modules'],
			alias: {
				config: path.resolve(__dirname, 'config.js')
			}
		},
		plugins: [
			new webpack.DefinePlugin({
				ENV_DEVELOPMENT: process.env.NODE_ENV === 'development',
				RELEASE: `"${process.env.RELEASE}"`
			})
		],
	},
	css: {
		loaderOptions: {
			stylus: {
				use: [require('buntpapier/stylus')({implicit: false})],
				import: ['~buntpapier/buntpapier/index.styl', '~variables']
			}
		}
	},
	lintOnSave: true
}