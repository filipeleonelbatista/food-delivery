import React from 'react';
import { Item, Input, Icon, Label } from 'native-base';

class PasswordInput extends React.Component{
    state = {
        icon: 'eye-off',
        password: true,
        isFocused: false,
    };

    _changeIcon(){
        this.setState(prevState =>({
            icon: prevState.icon === 'eye' ? 'eye-off' : 'eye',
            password: !prevState.password
        }));
    }

    handleFocus = event =>{
        this.setState({ isFocused: true })
        if(this.props.onFocus){
            this.props.onFocus(event);
        }
    };
    handleBlur = event =>{
        this.setState({ isFocused: false })
        if(this.props.onBlur){
            this.props.onBlur(event);
        }
    };

    render(){
        const { isFocused } = this.state;
        const { label, icon, onChange } = this.props;
        return(
            <Item floatingLabel>
                {/* <Icon active name={icon} /> */}
                <Label>{label}</Label>
                <Input
                    selectionColor={ isFocused ? "#E20030" : "#D3D3D3"} 
                    underlineColorAndroid={ isFocused ? "#E20030" : "#D3D3D3"} 
                    onFocus={this.handleFocus}
                    onBlur={this.handleBlur} 
                    secureTextEntry={this.state.password} 
                    onChangeText={(e) => { onChange(e)}} />
                <Icon name={this.state.icon} onPress={() => this._changeIcon()} />
            </Item>
        );
    }
}

export default PasswordInput; 