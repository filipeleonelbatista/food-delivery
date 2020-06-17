import React, { BackHandler } from 'react';
import { StyleSheet, View } from 'react-native';
import {
  useTheme,
  Avatar,
  Title,
  Caption,
  Paragraph,
  Drawer,
  Text,
  TouchableRipple,
  Switch
} from 'react-native-paper';
import {
  DrawerContentScrollView,
  DrawerItem
} from '@react-navigation/drawer';

import Icon from 'react-native-vector-icons/FontAwesome5';

import Toast from 'react-native-tiny-toast'

export default function DrawerContent(props) {
  const paperTheme = useTheme();
  function handleExit() {
    Toast.show('Saindo da aplicação')
    props.navigation.navigate('LoginScreen')
  }
  return (
    <View style={{ flex: 1 }}>
      <DrawerContentScrollView {...props}>
        <View style={styles.drawerContent}>
          <View style={styles.userInfoSection}>
            <View style={{ flexDirection: 'row', marginTop: 15 }}>
              <Avatar.Image
                source={{
                  uri: 'https://api.adorable.io/avatars/50/abott@adorable.png'
                }}
                size={50}
              />
              <View style={{ marginLeft: 15, flexDirection: 'column' }}>
                <Title style={styles.title}>Administrador</Title>
                <Caption style={styles.caption}>Adm. do sistema</Caption>
              </View>
            </View>

            <View style={styles.row}>
              <View style={styles.section}>
                <Paragraph style={[styles.paragraph, styles.caption]}>80</Paragraph>
                <Caption style={styles.caption}>Pendentes</Caption>
              </View>
              <View style={styles.section}>
                <Paragraph style={[styles.paragraph, styles.caption]}>100</Paragraph>
                <Caption style={styles.caption}>Em prdução</Caption>
              </View>
            </View>
          </View>

          <Drawer.Section style={styles.drawerSection}>
            <DrawerItem
              icon={({ color, size }) => (
                <Icon
                  name="id-badge"
                  color={color}
                  size={size}
                />
              )}
              label="Perfil"
              onPress={() => { }}
            />
          </Drawer.Section>

          <Drawer.Section style={styles.drawerSection}>
            <DrawerItem
              icon={({ color, size }) => (
                <Icon
                  name="tachometer-alt"
                  color={color}
                  size={size}
                />
              )}
              label="Página inicial"
              onPress={() => { props.navigation.navigate('Home') }}
            />
          </Drawer.Section>
          <Drawer.Section style={styles.drawerSection}>
            <DrawerItem
              icon={({ color, size }) => (
                <Icon
                  name="cash-register"
                  color={color}
                  size={size}
                />
              )}
              label="Vendas"
              onPress={() => { }}
            />
            <DrawerItem
              icon={({ color, size }) => (
                <Icon
                  name="users"
                  color={color}
                  size={size}
                />
              )}
              label="Clientes"
              onPress={() => { }}
            />
            <DrawerItem
              icon={({ color, size }) => (
                <Icon
                  name="file-alt"
                  color={color}
                  size={size}
                />
              )}
              label="Pedidos"
              onPress={() => { }}
            />
            <DrawerItem
              icon={({ color, size }) => (
                <Icon
                  name="boxes"
                  color={color}
                  size={size}
                />
              )}
              label="Produtos"
              onPress={() => { }}
            />
            <DrawerItem
              icon={({ color, size }) => (
                <Icon
                  name="motorcycle"
                  color={color}
                  size={size}
                />
              )}
              label="Entregas"
              onPress={() => { }}
            />
            <DrawerItem
              icon={({ color, size }) => (
                <Icon
                  name="utensils"
                  color={color}
                  size={size}
                />
              )}
              label="Cosinha"
              onPress={() => { }}
            />
          </Drawer.Section>

          <Drawer.Section style={styles.drawerSection}>
            <DrawerItem
              icon={({ color, size }) => (
                <Icon
                  name="user-friends"
                  color={color}
                  size={size}
                />
              )}
              label="Usuários"
              onPress={() => { }}
            />
          </Drawer.Section>

          {/* <Drawer.Section title="Preferences">
                        <TouchableRipple onPress={() => {toggleTheme()}}>
                            <View style={styles.preference}>
                                <Text>Dark Theme</Text>
                                <View pointerEvents="none">
                                    <Switch value={paperTheme.dark}/>
                                </View>
                            </View>
                        </TouchableRipple>
                    </Drawer.Section> */}
        </View>
      </DrawerContentScrollView>
      <Drawer.Section style={styles.bottomDrawerSection}>
        <DrawerItem
          icon={({ color, size }) => (
            <Icon
              name="sign-out-alt"
              color={color}
              size={size}
            />
          )}
          label="Sair"
          onPress={() => { handleExit() }}
        />
      </Drawer.Section>
    </View>
  );
}

const styles = StyleSheet.create({
  drawerContent: {
    flex: 1,
  },
  userInfoSection: {
    paddingLeft: 20,
  },
  title: {
    fontSize: 16,
    marginTop: 3,
    fontWeight: 'bold',
  },
  caption: {
    fontSize: 14,
    lineHeight: 14,
  },
  row: {
    marginTop: 20,
    flexDirection: 'row',
    alignItems: 'center',
  },
  section: {
    flexDirection: 'row',
    alignItems: 'center',
    marginRight: 15,
  },
  paragraph: {
    fontWeight: 'bold',
    marginRight: 3,
  },
  drawerSection: {
    marginTop: 15,
  },
  bottomDrawerSection: {
    marginBottom: 15,
    borderTopColor: '#f4f4f4',
    borderTopWidth: 1
  },
  preference: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    paddingVertical: 12,
    paddingHorizontal: 16,
  },
});