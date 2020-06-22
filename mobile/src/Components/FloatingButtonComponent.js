import * as React from 'react';
import { FAB, Portal } from 'react-native-paper';

export default class FloatingButtonComponent extends React.Component {
  state = {
    open: false,
  };

  render() {
    return (
      <Portal>
        <FAB.Group
        fabStyle={ this.state.open ? { backgroundColor:'#D20030' } : { backgroundColor:'#E20030' } }
          open={this.state.open}
          icon={this.state.open ? 'close' : 'plus'}
          actions={[
            { icon: 'file-document-outline', label: 'Novo pedido', onPress: () => console.log('Novo pedido')},
            { icon: 'account', label: 'Novo Cliente', onPress: () => console.log('Novo Cliente') },
            { icon: 'food', label: 'Novo Prato', onPress: () => console.log('Novo Prato') },
          ]}
          onStateChange={({ open }) => this.setState({ open })}
          onPress={() => {
            if (this.state.open) {
              // do something if the speed dial is open
            }
          }}
        />
      </Portal>
    );
  }
}