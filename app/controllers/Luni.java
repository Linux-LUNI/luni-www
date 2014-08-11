package controllers;

import play.*;
import play.mvc.*;

import views.html.*;


/**
 * Created by user on 8/10/14.
 */
public class Luni extends Controller {

	//LUNI site
	public static Result contactus() {
		return ok(contactus.render());
	}


	public static Result calendar() {
		return ok(calendar.render());
	}


	public static Result orgs() {
		return ok(orgs.render());
	}

	public static Result home() {
		return ok(home.render());
	}

}
