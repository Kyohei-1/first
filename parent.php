<?php

// class OBJ{
// 	public static $name = '名無し';
// 	public $hp = 30;
// 	public function attack(){
// 		return 1;
// 	}
// 	public static function magicAttack(){
// 		return 2;
// 	}
// }

// $monst = new OBJ();
// echo $monst->hp.'<br>';
// // echo $monst->name; //静的メンバなので、インスタンスからアクセスできない
// echo OBJ::$name . '<br>';
// echo $monst->attack() . '<br>';
// echo OBJ::magicAttack() . '<br>';

// echo $monst->hp . '<br>';
// echo OBJ::$name . '<br>';
// echo $monst->attack() . '<br>';
// echo OBJ::magicAttack() . '<br>';

# クラス定数

abstract class Sex{
	//クラス定数を用意
	const MAN = '男';
	const WOMAN = '女';

	//静的メンバでメソッドを作る
	abstract public function p_data();


}

class Other extends Sex{
	const OTHER = 'その他';
	public function p_data_a()
	{
		return self::OTHER;
	}

	public function p_data()
	{
		echo Sex::WOMAN;
	}
}

$other = new Other();

// $sex = new Sex();

echo $other->p_data_a();

// echo Sex::p_data();

echo Sex::MAN;

// echo $sex->p_data();
