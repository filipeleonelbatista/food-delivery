import React from 'react';
import { StyleSheet, Text, View, ScrollView, ImageBackground, Dimensions } from 'react-native';

import { TouchableOpacity } from 'react-native-gesture-handler';

import Icon from 'react-native-vector-icons/MaterialCommunityIcons';

import Pizza from '../../Assets/PNGIcons/pizza.png'

import { ProgressBar, Colors, FAB } from 'react-native-paper';

import { BarChart, PieChart } from "react-native-chart-kit";

import FloatingButtonComponent from '../../Components/FloatingButtonComponent'

const screenWidth = Dimensions.get("window").width;

export default function Home({ route, navigation }) {
    let email = route.params.email;
    let password = route.params.password;

    const data = {
        labels: ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"],
        datasets: [
            {
                data: [20, 45, 68, 80, 99, 73, 43]
            }
        ]
    };
    const data2 = [
        {
            name: "Aguardando confirmação",
            qtdPedidos: 3,
            color: "#E20030",
            legendFontColor: "#7F7F7F",
            legendFontSize: 15
        },
        {
            name: "Abertos",
            qtdPedidos: 5,
            color: "#38a2b8",
            legendFontColor: "#7F7F7F",
            legendFontSize: 15
        },
        {
            name: "Em produção",
            qtdPedidos: 12,
            color: "#3279fd",
            legendFontColor: "#7F7F7F",
            legendFontSize: 15
        },
        {
            name: "Saiu para entrega",
            qtdPedidos: 24,
            color: "#f9c116",
            legendFontColor: "#7F7F7F",
            legendFontSize: 15
        },
        {
            name: "Concluído",
            qtdPedidos: 32,
            color: "#3ca84b",
            legendFontColor: "#7F7F7F",
            legendFontSize: 15
        }
    ];

    const chartConfig = {
        backgroundColor: "#FFF",
        backgroundGradientFrom: "#FFF",
        backgroundGradientTo: "#FFF",
        decimalPlaces: 2,
        color: (opacity = 1) => `rgba(255, 0, 0, ${opacity})`,
        labelColor: (opacity = 1) => `rgba(0, 0, 0, ${opacity})`,
        style: {
            borderRadius: 16,
        },
        propsForDots: {
            r: "6",
            strokeWidth: "2",
            stroke: "#ffa726"
        }
    };



    return (
        <>

            <View style={styles.header}>
                <View style={[styles.headerTextContainer, styles.alignVertical]}>
                    <TouchableOpacity
                        onPress={() => { navigation.openDrawer(); }}
                        activeOpacity={0.6}
                        style={styles.headerButton}
                    >
                        <View style={styles.notification}>
                            <Text style={styles.notificationText}>1</Text>
                        </View>
                        <Icon
                            name="hamburger"
                            color={'#fff'}
                            size={35}
                        />
                    </TouchableOpacity>
                    <Text style={[{ flex: 1, textAlign: 'center' }, styles.headerText]}>Página inicial</Text>
                    <View
                        style={styles.headerButton}
                    />
                </View>

            </View>

            <ScrollView
                vertical
                showsHorizontalScrollIndicator={true}>
                <View style={styles.headerTextContainer}>
                    <Text style={styles.textTitle}>Acesso Rápido</Text>
                </View>
                <View>
                    <ScrollView
                        horizontal
                        showsHorizontalScrollIndicator={false}
                        contentContainerStyle={{
                            paddingHorizontal: 5
                        }}>

                        <TouchableOpacity
                            onPress={() => { }}
                            activeOpacity={0.6}
                            style={styles.item}
                        >
                            <View style={styles.notification}>
                                <Text style={styles.notificationText}>1</Text>
                            </View>
                            <Icon
                                name="cash"
                                color={'#bbbbbbbb'}
                                size={32}
                            />
                            <Text style={{ fontSize: 12 }}>Pedidos</Text>
                        </TouchableOpacity>

                        <TouchableOpacity
                            onPress={() => { }}
                            activeOpacity={0.6}
                            style={styles.item}
                        >
                            <Icon
                                name="account-group"
                                color={'#bbbbbbbb'}
                                size={32}
                            />
                            <Text style={{ fontSize: 12 }}>Clientes</Text>
                        </TouchableOpacity>

                        <TouchableOpacity
                            onPress={() => { }}
                            activeOpacity={0.6}
                            style={styles.item}
                        >
                            <Icon
                                name="inbox-multiple"
                                color={'#bbbbbbbb'}
                                size={32}
                            />
                            <Text style={{ fontSize: 12 }}>Cardápio</Text>
                        </TouchableOpacity>

                        <TouchableOpacity
                            onPress={() => { }}
                            activeOpacity={0.6}
                            style={styles.item}
                        >
                            <Icon
                                name="truck-delivery"
                                color={'#bbbbbbbb'}
                                size={32}
                            />
                            <Text style={{ fontSize: 12 }}>Entregas</Text>
                        </TouchableOpacity>

                        <TouchableOpacity
                            onPress={() => { }}
                            activeOpacity={0.6}
                            style={styles.item}
                        >
                            <Icon
                                name="food"
                                color={'#bbbbbbbb'}
                                size={32}
                            />
                            <Text style={{ fontSize: 12 }}>Cozinha</Text>
                        </TouchableOpacity>

                    </ScrollView>
                </View>

                <View>
                    <View style={styles.headerTextContainer}>
                        <Text style={styles.textTitle}>Relatórios</Text>
                    </View>
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
                    <View style={styles.graphContainer}>
                        <Text style={[styles.textTitle, { marginBottom: 5 }]}>Pedidos concluídos</Text>
                        <BarChart
                            data={data}
                            width={screenWidth - 30}
                            height={210}
                            yAxisLabel="R$"
                            chartConfig={chartConfig}
                            withVerticalLabels
                            showValuesOnTopOfBars
                            fromZero
                        />
                    </View>
                    <View style={styles.graphContainer}>
                        <Text style={[styles.textTitle, { marginBottom: 5 }]}>Pedidos por status</Text>
                        <PieChart
                            data={data2}
                            width={screenWidth - 30}
                            height={220}
                            chartConfig={chartConfig}
                            accessor="qtdPedidos"
                            backgroundColor="transparent"
                            paddingLeft="15"
                            absolute
                        />
                    </View>
                </View>
            </ScrollView>

            <FloatingButtonComponent />
        </>
    );
}

const styles = StyleSheet.create({
    floatingButtom: {
        position: 'absolute',
        margin: 16,
        right: 0,
        bottom: 0,
        backgroundColor: '#E20030',
    },
    notification: {
        position: 'absolute',
        top: 8,
        right: 8,
        width: 16,
        height: 16,
        borderRadius: 8,
        backgroundColor: "#E20030",
        shadowColor: "#FFF",
        shadowOffset: {
            width: 0,
            height: 3,
        },
        shadowOpacity: 0.25,
        shadowRadius: 3.84,

        elevation: 6,
        alignItems: 'center',
        justifyContent: 'center',
    },
    notificationText: {
        color: "#FFF",
        fontSize: 10,
    },
    graphContainer: {
        width: screenWidth - 20,
        height: 270,
        backgroundColor: "#FFF",
        borderRadius: 16,
        marginLeft: 10,
        marginRight: 10,
        marginBottom: 8,
        padding: 5,
        shadowColor: "#FFF",
        shadowOffset: {
            width: 0,
            height: 3,
        },
        shadowOpacity: 0.25,
        shadowRadius: 3.84,

        elevation: 8,
    },
    headerButton: {
        height: 56,
        width: 56,
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
        height: 56,
        backgroundColor: "#E20030",
        flexDirection: 'column',
        alignItems: "center",
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
        height: 56
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
        marginRight: 10,
        color: "#FFF",
        fontWeight: 'bold',
        fontSize: 20,
    },
    container: {
        flexDirection: 'column'
    },
    itemsContainer: {
        flexDirection: 'row',
    },
    item: {
        backgroundColor: '#fff',
        height: 80,
        width: 80,
        borderRadius: 40,
        marginTop: 8,
        marginRight: 8,
        marginLeft: 8,
        marginBottom: 8,
        alignItems: 'center',
        justifyContent: 'center',
        shadowColor: "#000",
        shadowOffset: {
            width: 0,
            height: 3,
        },
        shadowOpacity: 0.25,
        shadowRadius: 3.84,

        elevation: 8,
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
});
