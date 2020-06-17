import React from 'react';
import { StyleSheet, Image, View } from 'react-native';

import Logo from '../../Assets/logo.png';

export default function Splash() {

    return (
        <View style={styles.container}>
            <View style={styles.imageContainer}>
                <Image
                    source={Logo}
                    style={styles.logo} />
            </View>
        </View>

    );
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#fff',
        flexDirection: 'column',
    },
    imageContainer: {
        alignItems: 'center',
        justifyContent: 'center',
        flex: 1,
    },
    logo: {
        height: 166,
        width: 200,
        padding: 2

    }
});
