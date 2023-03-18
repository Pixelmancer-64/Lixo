import { watch } from 'chokidar';

const watcher = watch('/', {
  persistent: true,
  ignored: /[\/\\]\./, // ignore dotfiles
  ignoreInitial: true, // don't fire events for existing files/directories
});

watcher
  .on('add', (path) => console.log(`File ${path} has been added`))
  .on('change', (path) => console.log(`File ${path} has been changed`))
  .on('unlink', (path) => console.log(`File ${path} has been removed`))
  .on('addDir', (path) => console.log(`Directory ${path} has been added`))
  .on('unlinkDir', (path) => console.log(`Directory ${path} has been removed`))
  .on('error', (error) => console.error(`Watcher error: ${error}`));
