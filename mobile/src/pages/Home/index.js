import React from 'react';
import { StyleSheet, Text, View, ScrollView, ImageBackground } from 'react-native';

import { TouchableOpacity } from 'react-native-gesture-handler';

import Icon from 'react-native-vector-icons/MaterialCommunityIcons';

import Pizza from '../../Assets/PNGIcons/pizza.png'

import { ProgressBar, Colors } from 'react-native-paper';

export default function Home({ route, navigation }) {
    let email = route.params.email;
    let password = route.params.password;

    return (
        <>

            <View style={styles.header}>
                <View style={[styles.headerTextContainer, styles.alignVertical]}>
                    <TouchableOpacity
                        onPress={() => { navigation.openDrawer(); }}
                        activeOpacity={0.6}
                        style={styles.headerButton}
                    >

                        <Icon
                            name="hamburger"
                            color={'#fff'}
                            size={32}
                        />
                    </TouchableOpacity>
                    <Text style={styles.headerText}>Olá,</Text>
                    <Text style={styles.headerText}>Fulano de tal </Text>
                </View>

            </View>


            <View style={styles.container}>

                <View style={styles.headerTextContainer}>
                    <Text style={styles.textTitle}>Acesso Rápido</Text>
                </View>
                <View>
                    <ScrollView
                        horizontal
                        showsHorizontalScrollIndicator={false}
                        contentContainerStyle={{
                            paddingHorizontal: 20
                        }}>

                        <TouchableOpacity
                            onPress={() => { }}
                            activeOpacity={0.6}
                            style={styles.item}
                        >
                            <Icon
                                name="cash"
                                color={'#bbbbbbbb'}
                                size={32}
                            />
                            <Text>Pedidos</Text>
                        </TouchableOpacity>

                    </ScrollView>
                </View>
                <View style={styles.headerTextContainer}>
                    <Text style={styles.textTitle}>Relatórios</Text>
                </View>
                <ScrollView
                    vertical
                    showsHorizontalScrollIndicator={true}
                    contentContainerStyle={{
                        paddingHorizontal: 20
                    }}>

                    <View
                        style={styles.cardRow}>

                        <View
                            style={[styles.cardRowItem, styles.bdColorDanger, styles.column]}
                        >
                            <View style={[styles.fx05, styles.alignVertical, styles.alignHorizontal, styles.row]}>
                                <View style={styles.alignHorizontal}>
                                    <Text style={styles.cardTextTitle}>Ganhos Diários</Text>
                                </View>
                            </View>
                            <View style={[styles.fx1, styles.alignVertical, styles.alignHorizontal, styles.row, { justifyContent: 'space-evenly' }]}>
                                <View>
                                    <Text style={styles.cardTextValue}>R$ 150,00</Text>
                                </View>
                                <Icon
                                    name="cash"
                                    color={'#bbbbbbbb'}
                                    size={32}
                                />
                            </View>
                        </View>

                        <View
                            style={[styles.cardRowItem, styles.bdColorDanger, styles.column]}
                        >
                            <View style={[styles.fx05, styles.alignVertical, styles.alignHorizontal, styles.row]}>
                                <View style={styles.alignHorizontal}>
                                    <Text style={styles.cardTextTitle}>Ganhos Mensais</Text>
                                </View>
                            </View>
                            <View style={[styles.fx1, styles.alignVertical, styles.alignHorizontal, styles.row, { justifyContent: 'space-evenly' }]}>
                                <View>
                                    <Text style={styles.cardTextValue}>R$ 150,00</Text>
                                </View>
                                <Icon
                                    name="cash-100"
                                    color={'#bbbbbbbb'}
                                    size={32}
                                />
                            </View>
                        </View>

                    </View>

                    <View
                        style={[styles.card, styles.bdColorSuccess]}
                    >
                        <View style={[styles.fx1, styles.alignVertical, styles.alignHorizontal, styles.row, { justifyContent: 'space-evenly' }]}>
                            <View style={[styles.column]}>

                                <Text style={styles.cardTextTitle}>Pedidos Concluídos</Text>
                                <Text style={styles.cardTextValue}>5/12</Text>
                                <ProgressBar progress={0.41} color={Colors.green800} />
                            </View>
                            <View style={[styles.column]}>
                                <Icon
                                    name="file-table-outline"
                                    color={'#bbbbbbbb'}
                                    size={32}
                                />
                            </View>
                        </View>

                    </View>

                    <View
                        style={styles.cardRow}>

                        <View
                            style={[styles.cardRowItem, styles.bdColorPrimary, styles.column]}
                        >
                            <View style={[styles.fx05, styles.alignVertical, styles.alignHorizontal, styles.row]}>
                                <View style={styles.alignHorizontal}>
                                    <Text style={styles.cardTextTitle}>Na cozinha</Text>
                                </View>
                            </View>
                            <View style={[styles.fx1, styles.alignVertical, styles.alignHorizontal, styles.row, { justifyContent: 'space-evenly' }]}>
                                <View>
                                    <Text style={styles.cardTextValue}>8</Text>
                                </View>
                                <Icon
                                    name="food"
                                    color={'#bbbbbbbb'}
                                    size={32}
                                />
                            </View>
                        </View>

                        <View
                            style={[styles.cardRowItem, styles.bdColorPrimary, styles.column]}
                        >
                            <View style={[styles.fx05, styles.alignVertical, styles.alignHorizontal, styles.row]}>
                                <View style={styles.alignHorizontal}>
                                    <Text style={styles.cardTextTitle}>Para entrega</Text>
                                </View>
                            </View>
                            <View style={[styles.fx1, styles.alignVertical, styles.alignHorizontal, styles.row, { justifyContent: 'space-evenly' }]}>
                                <View>
                                    <Text style={styles.cardTextValue}>10</Text>
                                </View>
                                <Icon
                                    name="truck-delivery"
                                    color={'#bbbbbbbb'}
                                    size={32}
                                />
                            </View>
                        </View>

                    </View>

                </ScrollView>
            </View>

        </>
    );
}

const styles = StyleSheet.create({
    headerButton: {
        height: 48,
        width: 48,
        backgroundColor: '#E20030',
        justifyContent: 'center',
        alignItems: 'center',
    },
    fx1: {
        flex: 1,
    },
    fx05: {
        flex: 0.5,
    },
    alignHorizontal: {
        justifyContent: 'center'
    },
    alignVertical: {
        alignItems: 'center'
    },
    row: {
        flexDirection: 'row'
    },
    column: {
        flexDirection: 'column'
    },
    mr4: {
        marginTopt: 4,
    },
    mb4: {
        marginBottom: 4,
    },
    mr4: {
        marginRight: 4,
    },
    ml4: {
        marginLeft: 4,
    },
    header: {
        height: 48,
        backgroundColor: "#E20030",
        flexDirection: 'column',
        marginBottom: 8,
        shadowColor: "#000",
        shadowOffset: {
            width: 0,
            height: 3,
        },
        shadowOpacity: 0.25,
        shadowRadius: 3.84,

        elevation: 8,
    },
    headerTextContainer: {
        flexDirection: 'row',
        marginBottom: 16,
    },
    cardTextTitle: {
        color: "#E20030",
        fontWeight: 'normal',
        fontSize: 16
    },
    cardTextValue: {
        color: "#000",
        fontWeight: 'bold',
        fontSize: 20
    },
    textTitle: {
        marginTop: 10,
        marginLeft: 10,
        color: "#000",
        fontWeight: 'bold',
        fontSize: 22
    },
    headerText: {
        marginLeft: 10,
        color: "#FFF",
        fontWeight: 'bold',
        fontSize: 26
    },
    container: {
        flexDirection: 'column'
    },
    itemsContainer: {
        flexDirection: 'row',
        marginTop: 16,
        marginBottom: 32,
    },
    item: {
        backgroundColor: '#fff',
        height: 96,
        width: 96,
        borderRadius: 48,
        marginRight: 8,
        alignItems: 'center',
        justifyContent: 'center',
    },
    selectedItem: {
        borderColor: '#E20030',
    },
    itemImage: {
        width: 42,
        height: 42,
        alignItems: 'center',
        justifyContent: 'center',
    },
    cardRow: {
        flexDirection: 'row',
    },
    bdColorRed: {
        borderLeftColor: '#E20030',
    },
    bdColorPrimary: {
        borderLeftColor: '#3279fd',
    },
    bdColorSecondary: {
        borderLeftColor: '#6d757d',
    },
    bdColorSuccess: {
        borderLeftColor: '#3ca84b',
    },
    bdColorDanger: {
        borderLeftColor: '#d43140',
    },
    bdColorWarning: {
        borderLeftColor: '#f9c116',
    },
    bdColorInfo: {
        borderLeftColor: '#38a2b8',
    },
    bdColorDark: {
        borderLeftColor: '#353a40',
    },
    cardRowItem: {
        flex: 1,
        margin: 10,
        backgroundColor: '#FFF',
        height: 80,
        borderRadius: 8,
        borderLeftWidth: 4,
        shadowColor: "#000",
        shadowOffset: {
            width: 0,
            height: 2,
        },
        shadowOpacity: 0.25,
        shadowRadius: 3.84,

        elevation: 5,

    },
    card: {
        flex: 1,
        margin: 10,
        backgroundColor: '#FFF',
        height: 100,
        borderRadius: 8,
        borderLeftWidth: 4,
        shadowColor: "#000",
        shadowOffset: {
            width: 0,
            height: 2,
        },
        shadowOpacity: 0.25,
        shadowRadius: 3.84,

        elevation: 5,

    }
});
