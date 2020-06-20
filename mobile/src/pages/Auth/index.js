import React, { useState } from 'react';
import { StyleSheet, Linking, KeyboardAvoidingView, TextInput, Text, View, Image, Alert, Platform, ImageBackground } from 'react-native';
import { RectButton } from 'react-native-gesture-handler';

import PasswordInput from '../../Components/PasswordInput';
import TextInputStyled from '../../Components/TextInputStyled';

import { Feather as Icon } from '@expo/vector-icons';

import { useNavigation } from '@react-navigation/native';

import Logo from '../../Assets/logo.png';
import LoginBackground from '../../Assets/loginBackground.jpg';

const user = {
    email: '',
    password: '',
}

export default function LoginScreen() {

    const navigation = useNavigation();


    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    function handleNavigateToHome() {

        if ((user.email === email) && (user.password === password)) {
            navigation.navigate('Root', { screen: 'Home', params: { email, password } });
        } else {
            Alert.alert(
                "Ops...",
                "Usuário ou senha incorretos!",
                [
                    { text: "OK", onPress: () => console.log("OK Pressed") }
                ],
                { cancelable: false }
            );
        }
    }

    return (
        <ImageBackground source={LoginBackground} style={styles.image}>
            <KeyboardAvoidingView style={{ flex: 1 }} behavior={Platform.OS === 'ios' ? 'padding' : undefined}>
                <View style={styles.container}>
                    <Image style={styles.img} source={Logo} />

                    <View style={styles.form}>
                        <View style={styles.box}>
                            <Text style={{
                                color: '#888',
                                textAlign: 'center',
                                fontSize: 18
                            }} >
                                Entre com seu email ou senha ou
                        </Text>
                            <Text style={{
                                color: '#E20030',
                                textAlign: 'center',
                                fontSize: 18
                            }}
                                onPress={() => {
                                    Linking.openURL('https://google.com')
                                }} >
                                Cadastre-se Aqui!
                        </Text>

                            <View style={{ marginTop: 16 }}>
                                <TextInputStyled label="Email" onChange={setEmail} />
                            </View>
                            <View style={{ marginTop: 16 }}>
                                <PasswordInput label="Senha" onChange={setPassword} />
                            </View>

                            <Text style={styles.forgot} >
                                Esqueceu a senha?
                        </Text>
                            
                        </View>
                        <RectButton style={styles.button} onPress={handleNavigateToHome} >
                                <View style={styles.buttonIcon}>
                                    <Text>
                                        <Icon name="log-in" color="#fff" size={24} />
                                    </Text>
                                </View>
                                <Text style={styles.buttonText}>Entrar</Text>
                            </RectButton>
                    </View>
                </View>
            </KeyboardAvoidingView>
        </ImageBackground>
    );
}

const styles = StyleSheet.create({
    image: {
        flex: 1,
        resizeMode: "cover",
        justifyContent: "center"
    },
    container: {
        flex: 1,
        alignItems: 'center',
        justifyContent: 'center',
    },
    forgot: {
        textAlign: 'right',
        color: '#E20030',
        fontSize: 14,
        fontWeight: 'bold',
        marginTop: 16,
    },

    img: {
        marginTop: 64,
        alignItems: 'center',
    },
    box: {
        backgroundColor: "#FFFFFF",
        padding: 16,
        borderRadius:8,
        shadowColor: "#000",
        shadowOffset: {
            width: 0,
            height: 3,
        },
        shadowOpacity: 0.25,
        shadowRadius: 3.84,

        elevation: 8,
    },
    form: {
        flex: 1,
        marginTop: 64,
        marginLeft: 8,
        marginRight: 8,
    },
    button: {
        flexDirection: 'row',
        overflow: 'hidden',
        alignItems: 'center',
        height: 64,
        backgroundColor: '#F42F2C',
        borderRadius: 32,
        marginTop: 64,
        shadowColor: 'rgba(255, 0, 0, 0.9)',
        shadowOpacity: 0.8,
        elevation: 6,
        shadowRadius: 15,
        shadowOffset: { width: 1, height: 13 },
    },
    buttonIcon: {
        height: 64,
        width: 64,
        borderTopStartRadius: 32,
        borderBottomStartRadius: 32,
        backgroundColor: 'rgba(0, 0, 0, 0.1)',
        justifyContent: 'center',
        alignItems: 'center'
    },
    buttonText: {
        flex: 1,
        justifyContent: 'center',
        textAlign: 'center',
        color: '#FFF',
        fontSize: 16,
    }
});
